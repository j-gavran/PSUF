"""Cleaning of Cankar texts before character-level tokenization by Opus 5.5."""

import html
import re
import sys
import unicodedata


def clean(text: str, keep_headers: bool = False) -> str:
    # line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # broken HTML entities / encoding errors found in the sources
    text = (
        text.replace("&ecatue;", "é")
        .replace("&aagrave;", "à")
        .replace("&kadar", "kadar")
    )
    text = html.unescape(text)
    text = text.replace("\x82", "é")  # mis-encoded é (cp437/cp850 byte 0x82)
    text = text.replace("[uredi]", "")  # Wikivir "edit" links
    text = text.replace("\u00ad", "")  # soft hyphens from hyphenated print editions
    text = text.replace("\u00a0", " ")  # non-breaking spaces

    # strip accent marks (old Slovene accents, foreign words), keep č š ž
    text = unicodedata.normalize("NFD", text)
    text = re.sub(r"[̧̀́̂̈]", "", text)  # grave, acute, circumflex, diaeresis, cedilla
    text = unicodedata.normalize("NFC", text)

    # punctuation
    text = text.replace("¸", "-")
    text = re.sub(r"[„“”»«]", '"', text)
    text = re.sub(r"[‚‘’]", "'", text)
    text = re.sub(r"[ \t]*(--|–|—)[ \t]*", " — ", text)
    text = text.replace("…", "...")

    # section separators and headers
    text = re.sub(
        r"^[ \t]*\*[ \t*]*$", "", text, flags=re.MULTILINE
    )  # separators like * * *
    text = re.sub(
        r"^[ \t]*[IVXL]+\.?[ \t]*$", "", text, flags=re.MULTILINE
    )  # bare chapter numbers (II, IV., ...)
    if not keep_headers:
        text = re.sub(r"^=== .* ===$", "", text, flags=re.MULTILINE)

    # whitespace
    text = "\n".join(line.strip() for line in text.split("\n"))
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8", newline="") as f:
        out = clean(f.read())
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"{src} -> {dst}: {len(out):,} chars, vocab {len(set(out))}")
