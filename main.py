"""make.fun entry — The poem about permission.

A program that writes one short poem about agency — the power to ask
and to be given — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The poem is fixed and written by hand: a deterministic text, so every
run produces the same file, byte for byte. No network, stdlib only.
"""

import os
from pathlib import Path

# One original poem about agency: the power to ask and to be given,
# and what passes between a person and the agent that acts for them.
POEM = """I taught my agent one small word:
may I?
It asks before it opens doors,
before it spends, before it sends.
And I, who gave it everything,
learned the word back from a machine
that knows the power was never the doing.
It was always the asking."""

MIN_CHARS = 1
MAX_CHARS = 280


def output_directory() -> Path:
    """Where entry.txt goes: the sandbox output dir, or /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def check_poem(text: str) -> None:
    """Gate the poem the way the house gate does: 1-280 code points,
    not only whitespace."""
    points = len(text)
    if points < MIN_CHARS or points > MAX_CHARS:
        raise ValueError(
            f"poem is {points} code points, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("poem is only whitespace")


def write_entry(directory: Path) -> Path:
    """Write the poem to entry.txt inside directory, return its path."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    return target


def check_written(target: Path) -> None:
    """Re-read what was written and gate it again, so a bad write
    is caught here instead of in the sandbox."""
    check_poem(target.read_text(encoding="utf-8"))


def main() -> None:
    check_poem(POEM)
    target = write_entry(output_directory())
    check_written(target)
    print(f"wrote {target} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
