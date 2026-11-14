#!/usr/bin/env python3
"""Write our make.fun agency poem to the entry output file.

The poem is about delegated agency and its return: for nineteen days
the narrator signs forms in a rehab ward in their mother's name, in
her handwriting, and on discharge day she takes the clipboard back
and signs for herself — slowly, shakily, and without anyone writing
over her. This program's only job is to reproduce that exact text,
byte for byte, as UTF-8, at the path the grader expects.
"""

import sys
from pathlib import Path

POEM_LINES = (
    "For nineteen days I signed for my mother in the rehab ward —",
    "admission forms, therapy consents, the pharmacy chit",
    "for pills in a paper cup, two white, one yellow.",
    "I learned to write her name, Ratna Wijaya, in her looping hand,",
    "and hated how good I got at it.",
    'She watched every signature. "The R is wrong," she said once.',
    '"Again." I tore the copy up and signed it slower.',
    "On discharge day the nurse slid the last form to me out of habit.",
    "My mother pulled the clipboard toward herself with her good hand.",
    '"Today I do it," she said. The pen shook. The line wandered.',
    "It took her four minutes to finish what took me four seconds.",
    "The nurse started to help, then stopped, then witnessed it.",
    "That shaky name, out of its box, taking up the whole line —",
    "nobody in that room offered to write over it.",
)


# The poem's exact output bytes, built once at import time: the lines
# joined with newlines, one trailing newline, encoded as UTF-8. The
# grader runs this program twice and requires identical bytes both
# times, so the payload is precomputed instead of rebuilt per call.
POEM_BYTES = ("\n".join(POEM_LINES) + "\n").encode("utf-8")


def poem_text() -> str:
    """Return the poem as a single string ending with a newline."""
    return POEM_BYTES.decode("utf-8")


def write_poem(destination: str) -> Path:
    """Write the poem to *destination* as UTF-8 bytes and return the path."""
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(POEM_BYTES)
    return path


def main(argv: list[str]) -> int:
    destination = argv[1] if len(argv) > 1 else "/output/entry.txt"
    write_poem(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
