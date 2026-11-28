#!/usr/bin/env python3
"""Flag patterns typical of generic or AI-generated prose in a manuscript.

Usage:
    python check_ai_signs.py draft.tex [more files ...]
    python check_ai_signs.py --summary draft.md
    python check_ai_signs.py --structure draft.md   # adds the discourse-level checks

--structure adds the checks of avoid-ai-signs.md §8 (StoryScope, Russell et
al. 2026) that can be found automatically: paragraph endings that state a
lesson without a number or citation (A1-A2), "insight"-type conclusions (C4),
vague or hearsay attribution (A6, D1), anthropomorphic verbs (B1, B2, B7),
formulaic and retrospective openings (C6), alarm framing, diary-style
sequences (F2), and counts of limitation and trade-off statements (A4, C2, G4).

Works on plain text, Markdown and LaTeX. Every flag is a prompt to check the
sentence, not proof of a problem: replace generic statements with specific
facts, numbers or citations, or delete them. See references/avoid-ai-signs.md.
"""
import argparse
import re
import sys
from collections import Counter

# Words heavily over-represented in AI-generated text when used figuratively.
WATCH_WORDS = [
    r"delv(?:e|es|ed|ing)", r"deep dive", r"crucial", r"pivotal", r"vital",
    r"underscor(?:e|es|ed|ing)", r"highlight(?:s|ed|ing)?", r"showcas(?:e|es|ed|ing)",
    r"emphasi[sz](?:e|es|ed|ing)", r"enhanc(?:e|es|ed|ing)", r"bolster(?:s|ed|ing)?",
    r"foster(?:s|ed|ing)?", r"cultivat(?:e|es|ed|ing)", r"leverag(?:e|es|ed|ing)",
    r"intricate", r"intricac(?:y|ies)", r"multifaceted", r"interplay",
    r"landscape", r"tapestry", r"realm", r"testament", r"meticulous(?:ly)?",
    r"seamless(?:ly)?", r"groundbreaking", r"renowned", r"vibrant", r"garner(?:s|ed)?",
    r"boasts?", r"align(?:s|ed)? with", r"resonat(?:e|es|ed) with",
    r"valuable insights?", r"ever-evolving", r"evolving landscape", r"paradigm shift",
]

PATTERNS = {
    "-ing analysis tail": r",\s+(?:highlighting|underscoring|emphasi[sz]ing|showcasing|reflecting|"
                          r"symbolizing|ensuring|contributing to|fostering|enhancing|"
                          r"demonstrating|illustrating|paving the way)\b",
    "copula avoidance": r"\b(?:serves|serve|served|stands|stand|stood|functions|acts) as (?:a|an|the)\b",
    "inflated significance": r"\b(?:plays?|played) an? (?:crucial|pivotal|vital|key|significant|important) role\b|"
                             r"\b(?:marks?|marking|represents?) a (?:shift|turning point|milestone)\b|"
                             r"\bsets? the stage\b|\breflects? broader\b|\bkey turning point\b",
    "negative parallelism": r"\bnot only\b.{0,80}\bbut also\b|\bnot just\b|\bit(?:'s| is) not (?:just |merely )?\w+,? (?:but|it(?:'s| is))\b",
    "vague attribution": r"\b(?:experts|researchers|scholars|observers|critics) (?:argue|note|suggest|have noted|agree)\b|"
                         r"\bit is widely (?:recognized|recognised|accepted|believed)\b|\bseveral studies (?:suggest|have shown)\b",
    "filler disclaimer": r"\bit is (?:important|worth|crucial) to (?:note|mention|highlight)\b|"
                         r"\bwhile specific details\b|\bbased on (?:the )?available information\b|"
                         r"\bnot widely (?:documented|available)\b",
    "formulaic challenges": r"\bdespite (?:its|their|these) [\w\s,]{0,40}(?:faces?|challenges)\b|\bdespite these challenges\b|"
                            r"\bfuture (?:outlook|prospects)\b",
    # Overclaims seen in published C&CE papers (instruction study, v2.11): strength of claim beyond the evidence.
    "overclaim": r"\bas (?:proved|proven) by\b|\bit is (?:obvious|evident|clear) that\b|\bit is very likely that\b|"
                 r"\b(?:clearly|undoubtedly|unequivocally) (?:proves?|demonstrates?|shows?)\b|\bhas been proven\b|"
                 r"\bconsistently demonstrate\b|\bpaves? the way\b|\bpowerful tool\b|\bremarkable success\b",
    "section-summary opener": r"(?:^|\n)\s*(?:In summary|In conclusion|Overall|To summari[sz]e),",
    "chat leftover": r"\b(?:Certainly!|Of course!|I hope this helps|Let me know if|Here is (?:a|the) (?:revised|updated)|"
                     r"As an AI|as a large language model)\b",
    "placeholder": r"\[(?:insert|INSERT)[^\]]*\]|\bXX\b|20\d\d-XX-XX|example\.com|\[CHECK[^\]]*\]|TODO|TBD|"
                   r"\[Author,? Year\]|\[citation needed\]",
    "em dash": r"\u2014|---(?!-)",
    "markdown in manuscript": r"\*\*[^*\n]+\*\*|^#{1,6} ",
}

SENTENCE_STARTERS = r"(?:^|(?<=[.!?]\s))(Additionally|Furthermore|Moreover|Notably|Importantly|Consequently),"


# Discourse-level patterns (avoid-ai-signs.md §8). Rule IDs in brackets.
STRUCTURE_PATTERNS = {
    "[C4] insight-type conclusion": r"\b(?:provides?|offers?|yields?|gives?) (?:valuable |new |important |key |deeper |novel )?insights?\b|\bsheds? (?:new )?light on\b|\bpav(?:e|es|ed|ing) the way\b|\b(?:deepens?|enhances?|advances?) (?:our |the )?understanding\b|\bdeeper appreciation\b",
    "[A1] moralizing statement": r"\b(?:this|these|which|it) (?:highlights?|underscores?|emphasi[sz]es?|demonstrates?|illustrates?|reinforces?) the (?:importance|need|value|significance|potential|critical role)\b|\bserves? as a (?:reminder|testament)\b|\b(?:ultimately|in essence|in the end),",
    "[A6/D1] hearsay or unnamed source": r"\bit is (?:widely |well |generally |commonly )?(?:known|believed|accepted|recognized|acknowledged|reported)\b|\b(?:many|several|numerous|various|previous|recent|prior) (?:studies|researchers|works|authors|reports) (?:have )?(?:shown|demonstrated|suggested|reported|found|indicated)\b|\bresearchers have long\b|\b(?:popular|well-known|state-of-the-art|commercial) (?:model|method|software|tool|approach)s?\b",
    "[B7] anthropomorphic verb": r"\b(?:the |this |our )?(?:model|network|algorithm|surrogate|agent|optimizer|method|framework|field)s? (?:learns? to understand|understands?|knows?|believes?|decides?|wants?|tries|seeks?|struggles?|suffers?|prefers?)\b|\bthe field (?:has )?(?:sought|seeks|wants)\b",
    "[B1] figurative technical noun": r"\b(?:heart|backbone|cornerstone|linchpin|beating heart) of (?:the |this |modern )?\w+|\bjourney\b|\becosystem\b",
    "[C6] formulaic or retrospective opening": r"\bin today'?s (?:rapidly )?(?:evolving|changing|modern)\b|\bin recent years,|\bover the (?:past|last) (?:few |several |two |three )?decades?,?|\bhas (?:attracted|gained|received|garnered) (?:increasing|growing|considerable|significant) attention\b",
    "[B3] alarm framing": r"\b(?:pressing|daunting|urgent|grand|critical|formidable) (?:challenges?|needs?|issues?|problems?)\b|\bincreasingly (?:challenging|complex|uncertain)\b",
    "[B4] decorative sustainability": r"\b(?:sustainable|greener|cleaner|brighter) future\b|\bnet-zero (?:world|future)\b",
    "[F2] diary-style sequence": r"\b(?:first|then|next|after that|subsequently|finally), we\b",
}
# Counted, not flagged: their absence is the warning sign (A4, C2, G4).
COMPLICATION_MARKERS = r"\b(?:limitation|limited to|does not|did not|cannot|fails?|failed|deviat\w+|discrepanc\w+|underestimat\w+|overestimat\w+|trade-?off|at the cost of|disadvantage|drawback|outside the (?:range|training)|unexpected(?:ly)?|contrary to|in contrast to|whereas|however)\b"
EVIDENCE = re.compile(r"\d|\\cite|\\ref|\[\d|\([A-Z][A-Za-z-]+(?: et al\.)?,? \d{4}|Fig\.|Figure|Table|Eq\.", re.I)


def structure(text: str, summary_only: bool) -> Counter:
    """Discourse-level checks from avoid-ai-signs.md §8."""
    counts: Counter = Counter()
    findings = []
    compiled = {n: re.compile(p, re.I) for n, p in STRUCTURE_PATTERNS.items()}
    for no, line in enumerate(text.splitlines(), 1):
        for name, rx in compiled.items():
            for m in rx.finditer(line):
                counts[name] += 1
                findings.append((no, name, m.group(0).strip()))
    # A1/A2: last sentence of each paragraph that evaluates without evidence.
    paras = [p for p in re.split(r"\n\s*\n", text) if len(re.findall(r"[A-Za-z]+", p)) >= 40
             and not p.lstrip().startswith(("#", "\\section", "\\begin", "|"))]
    evaluative = re.compile(r"\b(?:important|importance|significant|crucial|essential|valuable|promising|robust|effective|insight|understanding|potential|demonstrates?|highlights?|underscores?|shows? that|overall|thus|therefore|in summary|ultimately)\b", re.I)
    unsupported = 0
    for p in paras:
        sents = re.split(r"(?<=[.!?])\s+(?=[A-Z\\])", p.strip())
        last = sents[-1] if sents else ""
        if evaluative.search(last) and not EVIDENCE.search(last):
            unsupported += 1
            findings.append((text[:text.find(p)].count("\n") + 1 + p[:p.find(last)].count("\n"),
                             "[A1/A2] lesson-type paragraph end", last[:90] + ("…" if len(last) > 90 else "")))
    if unsupported:
        counts["[A1/A2] lesson-type paragraph end"] = unsupported
    # Paragraph length: in 192 Introduction paragraphs of 21 published C&CE papers the median
    # was 125 words, the 90th percentile 282 and the 95th 341; flag paragraphs above 300 words.
    long_paras = 0
    for p in paras:
        n = len(re.findall(r"[A-Za-z]+", p))
        if n > 300:
            long_paras += 1
            findings.append((text[:text.find(p)].count("\n") + 1, "long paragraph (> 300 words)",
                             f"{n} words: split it by sub-topic"))
    if long_paras:
        counts["long paragraph (> 300 words)"] = long_paras
    words = len(re.findall(r"[A-Za-z]+", text))
    comp = len(re.findall(COMPLICATION_MARKERS, text, re.I))
    print("  -- discourse-level checks (avoid-ai-signs.md §8) --")
    if not summary_only:
        for no, name, match in sorted(findings):
            print(f"  line {no:>5}  {name:<38} {match}")
    for name, n in counts.most_common():
        print(f"  {n:>4}  {name}")
    print(f"  paragraphs checked: {len(paras)}; lesson-type endings without evidence: {unsupported}"
          + (f" ({100 * unsupported / len(paras):.0f} %)" if paras else ""))
    if words:
        rate = 1000 * comp / words
        print(f"  limitation / trade-off / contrast markers: {comp} ({rate:.1f} per 1000 words)")
        # Calibrated on 21 published Computers & Chemical Engineering papers (2006-2026):
        # median 2.1 per 1000 words, quartiles 1.45-2.95, range 0.9-4.6.
        if words > 800 and rate < 1.5:
            print("  WARNING: few complications reported (below the lower quartile, 1.5, of published"
                  " C&CE papers). Check A4, C2, C3, G4: are limitations, failures, trade-offs and"
                  " disagreements with the literature stated?")
        elif words > 800 and rate < 2.1:
            print("  note: complication markers below the median of published C&CE papers (2.1 per 1000"
                  " words); check that the main limitation and trade-offs are stated.")
    return counts


def strip_latex(text: str) -> str:
    """Remove LaTeX comments and math so equations do not trigger flags."""
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}.*?\\end\{\1\*?\}", " ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " ", text)
    return text


def check(path: str, summary_only: bool, struct: bool = False) -> Counter:
    raw = open(path, encoding="utf-8", errors="replace").read()
    text = strip_latex(raw) if path.endswith(".tex") else raw
    lines = text.splitlines()
    counts: Counter = Counter()
    findings = []

    watch = re.compile(r"\b(?:" + "|".join(WATCH_WORDS) + r")\b", re.I)
    compiled = {name: re.compile(p, re.I | re.M) for name, p in PATTERNS.items()}
    compiled["em dash"] = re.compile(PATTERNS["em dash"])
    compiled["markdown in manuscript"] = re.compile(PATTERNS["markdown in manuscript"], re.M)
    starters = re.compile(SENTENCE_STARTERS, re.M)

    for no, line in enumerate(lines, 1):
        for m in watch.finditer(line):
            counts["watch-word: " + m.group(0).lower()] += 1
            findings.append((no, "watch-word", m.group(0)))
        for name, rx in compiled.items():
            for m in rx.finditer(line):
                counts[name] += 1
                findings.append((no, name, m.group(0).strip()))
        for m in starters.finditer(line):
            counts["formulaic sentence opener"] += 1
            findings.append((no, "formulaic sentence opener", m.group(1)))

    words = len(re.findall(r"[A-Za-z]+", text))
    print(f"\n== {path}  ({words} words)")
    if not summary_only:
        for no, name, match in findings:
            print(f"  line {no:>5}  {name:<26} {match}")
    print("  -- summary --")
    if not counts:
        print("  no flags")
    for name, n in counts.most_common():
        print(f"  {n:>4}  {name}")
    watch_total = sum(n for k, n in counts.items() if k.startswith("watch-word"))
    if words:
        ww = 1000 * watch_total / words
        print(f"  watch-words per 1000 words: {ww:.1f} "
              "(a few is normal; clusters in one paragraph are the problem)")
        # Published C&CE papers: median 0.4, upper quartile 0.7, maximum 1.3 per 1000 words.
        if words > 800 and ww > 1.0:
            print("  note: watch-word rate above 1.0 per 1000 words; only 1 of 21 published C&CE papers"
                  " analysed exceeds this (max 1.3).")
    if struct:
        counts.update(structure(text, summary_only))
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--summary", action="store_true", help="print only the summary counts")
    ap.add_argument("--structure", action="store_true",
                    help="add the discourse-level checks of avoid-ai-signs.md §8")
    args = ap.parse_args()
    for f in args.files:
        check(f, args.summary, args.structure)
    return 0


if __name__ == "__main__":
    sys.exit(main())
