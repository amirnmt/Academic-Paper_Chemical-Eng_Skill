#!/usr/bin/env python3
"""Flag patterns typical of generic or AI-generated prose in a manuscript.

Usage:
    python check_ai_signs.py draft.tex [more files ...]
    python check_ai_signs.py --summary draft.md

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
    "section-summary opener": r"(?:^|\n)\s*(?:In summary|In conclusion|Overall|To summari[sz]e),",
    "chat leftover": r"\b(?:Certainly!|Of course!|I hope this helps|Let me know if|Here is (?:a|the) (?:revised|updated)|"
                     r"As an AI|as a large language model)\b",
    "placeholder": r"\[(?:insert|INSERT)[^\]]*\]|\bXX\b|20\d\d-XX-XX|example\.com|\[CHECK[^\]]*\]|TODO|TBD|"
                   r"\[Author,? Year\]|\[citation needed\]",
    "em dash": r"\u2014|---(?!-)",
    "markdown in manuscript": r"\*\*[^*\n]+\*\*|^#{1,6} ",
}

SENTENCE_STARTERS = r"(?:^|(?<=[.!?]\s))(Additionally|Furthermore|Moreover|Notably|Importantly|Consequently),"


def strip_latex(text: str) -> str:
    """Remove LaTeX comments and math so equations do not trigger flags."""
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}.*?\\end\{\1\*?\}", " ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " ", text)
    return text


def check(path: str, summary_only: bool) -> Counter:
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
        print(f"  watch-words per 1000 words: {1000 * watch_total / words:.1f} "
              "(a few is normal; clusters in one paragraph are the problem)")
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--summary", action="store_true", help="print only the summary counts")
    args = ap.parse_args()
    for f in args.files:
        check(f, args.summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
