"""Famous last words of a phone at 1% battery.

Writes a single line — the phone's own dying words — to the output file.
Standard library only. Output is byte-identical on every run.
"""

import os

LAST_WORDS = "I spent my final percent keeping your screen lit for a video you weren't even watching."


def resolve_output_path():
    """Resolve the output path, in priority order."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LAST_WORDS + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
