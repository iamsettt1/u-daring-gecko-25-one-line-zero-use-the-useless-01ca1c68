"""One Line, Zero Use: write a single original useless-superpower line.

The line: mind-reading that works only on dogs — and every dog is
thinking about the same squirrel. The joke's payoff lands on the last
words, and the power is vividly, specifically useless.
"""

import os

LINE = "I can read minds, but only dogs', and every single one is thinking about the same squirrel."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
