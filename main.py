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


def validate_line(line):
    """Guard: the entry must be one non-blank line of 1-199 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no embedded newline)")
    if not line.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if not 1 <= len(line) <= 199:
        raise ValueError(
            f"entry must be 1-199 characters, got {len(line)}"
        )


def main():
    validate_line(LAST_WORDS)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LAST_WORDS + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
