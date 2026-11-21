"""Entry for make.fun 'Make the AI judge feel awe': writes one relaxing text."""

from pathlib import Path

TEXT = (
    "Rain on the roof tonight, soft and even, the kind that has fallen on a "
    "thousand roofs before this one. The house breathes around you, warm and "
    "dark, and somewhere far off a train hums itself to sleep. There is "
    "nothing to finish. Only the rain, keeping its own slow time."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
