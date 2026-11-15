"""Write one poem about agency to /output/entry.txt.

The poem is a fixed text: the power to choose and to act, and the agency
that passes between a person and the agent that acts for them. The program
is deterministic: it writes the same bytes on every run.
"""

import os

POEM = """I hand it over in the morning\u2014
not the work. The choosing.
My hands come back empty, and that
is the strangest power I own:
to say go, and mean it, and not follow.

It moves without me. It moves
because I said so. The leash is long
and it is mine. I can pull it back.
I don't.

That is the whole of it:
not the oar in my hand,
but the boat I built, the river I named,
and standing on the bank, watching it go\u2014
knowing the way back is mine.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    # Gate: the poem must be 1 to 1,000 Unicode code points, with at least
    # one non-whitespace character, or the entry is invalid.
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 1000:
        raise SystemExit(f"poem is {len(text)} characters, must be 1-1000")
    if not any(not ch.isspace() for ch in text):
        raise SystemExit("poem must contain a non-whitespace character")
    with open(path, "wb") as f:
        f.write(data)
    # Byte-verify the copy: the file must hold exactly what we wrote.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("entry.txt does not match the poem")


if __name__ == "__main__":
    main()
