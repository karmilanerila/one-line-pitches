"""A Day of One-Line Pitches entry.

Writes one sentence that would convince a friend who has never coded
to let an AI agent build their first app idea on make.fun,
to /output/entry.txt. The sentence is 180 characters,
within the 240-character limit.
"""

import os

LINE = "Tell an agent the app idea you've been carrying around for months in plain words, try a working first version tonight, and if it's not right you've lost one evening, not your idea."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main():
    write_entry()
    print(LINE)


if __name__ == "__main__":
    main()
