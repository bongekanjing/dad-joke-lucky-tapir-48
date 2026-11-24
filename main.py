"""Write one dad joke of at most 200 characters to entry.txt."""

import os

JOKE = (
    "I got a job at the library. My son asked what I do all day. "
    "I said, I check things out."
)

MAX_LEN = 200


def check(text):
    """Collapse whitespace runs and enforce the length limit."""
    cleaned = " ".join(text.split())
    if not cleaned:
        raise SystemExit("joke is blank after trimming whitespace")
    if len(cleaned) > MAX_LEN:
        raise SystemExit(
            "joke is %d characters, more than the %d character limit"
            % (len(cleaned), MAX_LEN)
        )
    return cleaned


def destination():
    """Return the path of the entry file."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    return os.path.join(base, "entry.txt")


def main():
    joke = check(JOKE)
    path = destination()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke + "\n")
    print(len(joke))
    print(path)


if __name__ == "__main__":
    main()
