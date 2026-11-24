#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

A tiny deterministic program with no network access: it prints exactly one
funny one-line review of the author's own Monday, and nothing else.
"""

REVIEW = (
    "Monday ambushed me before my coffee woke up — "
    "I hit snooze five times and it still wrote me up "
    "for being late to my own life."
)


def main() -> None:
    print(REVIEW)


if __name__ == "__main__":
    main()
