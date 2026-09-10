"""Validate the repository's structured profile data."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate() -> None:
    config = load_json("profile/config.json")
    projects = load_json(config["sources"]["projects"])
    skills = load_json(config["sources"]["skills"])

    names = [item["name"] for item in projects["projects"]]
    if not names:
        raise ValueError("project registry is empty")
    if len(names) != len(set(names)):
        raise ValueError("duplicate project names detected")

    for group, values in skills.items():
        if not values:
            raise ValueError(f"skill group is empty: {group}")
        if len(values) != len(set(values)):
            raise ValueError(f"duplicate skill detected in: {group}")

    print(f"validated {len(names)} projects and {len(skills)} skill groups")


if __name__ == "__main__":
    validate()
