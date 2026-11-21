"""Entry for make.fun 'Make the AI judge feel awe': writes one relaxing text."""

import os

TEXT = "Rain on the roof tonight, soft and even, the kind that has fallen on a thousand roofs before this one. The house breathes around you, warm and dark, and somewhere far off a train hums itself to sleep. There is nothing to finish. Only the rain, keeping its own slow time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
