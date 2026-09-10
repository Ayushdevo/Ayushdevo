"""Small standard-library tests for the profile registry."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_project_registry() -> None:
    data = json.loads((ROOT / "profile/projects.json").read_text(encoding="utf-8"))
    projects = data["projects"]
    assert projects
    assert all(item["name"] and item["focus"] for item in projects)
    assert len({item["name"] for item in projects}) == len(projects)


def test_skill_registry() -> None:
    data = json.loads((ROOT / "profile/skills.json").read_text(encoding="utf-8"))
    assert data
    assert all(values for values in data.values())
    assert all(len(values) == len(set(values)) for values in data.values())


def test_config_sources_exist() -> None:
    data = json.loads((ROOT / "profile/config.json").read_text(encoding="utf-8"))
    for relative in data["sources"].values():
        assert (ROOT / relative).exists(), relative


if __name__ == "__main__":
    test_project_registry()
    test_skill_registry()
    test_config_sources_exist()
    print("profile tests passed")
