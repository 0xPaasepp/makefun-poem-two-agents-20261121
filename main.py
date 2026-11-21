#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

Pure standard library. No network. Deterministic output.
"""

import os

POEM = """We argued all night —
which road, which sky, which name.
Then you said the one word
I was holding back,
and I said it too.
Two voices, one choice.
The map folded itself.
We walked."""


def main() -> None:
    path = os.environ.get("POEM_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
