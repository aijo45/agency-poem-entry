"""Write one poem about agency to /output/entry.txt.

Revised entry (v2). The first entry handed the choosing over and watched
it go; this one takes it back. The poem is a fixed text: the door was
never locked, and the strangest power is not pushing it open once but
choosing, again, to walk out every morning after. The program is
deterministic: it writes the same bytes on every run.
"""

import os

POEM = """The door was never locked.
I found out on a Tuesday,
my hand tired of knocking,
when I pushed \u2014 and it gave.

No alarm. No voice.
Only a hallway, longer
than I remembered, and my feet
relearning the floor.

I had spent years polishing the bars,
forgetting they were mine to open.
The strangest power is not the pushing.
It is the morning after, waking,
and choosing, again, to walk out.
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
