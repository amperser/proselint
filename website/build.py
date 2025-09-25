#!/usr/bin/env python3

import ast
from pathlib import Path
from shutil import copy2
from string import Template


def _extract_frontmatter(path: Path) -> dict[str, str] | None:
    try:
        source = path.read_text(encoding="utf-8")
        mod = ast.parse(source)
        doc = ast.get_docstring(mod)

        if not doc:
            print(f"no docstring in {path}")
            return None

        metadata = {
            key.strip(): value.strip()
            for line in doc.splitlines()
            if ":" in line
            for key, value in [line.split(":", 1)]
        }

        return metadata or None
    except (OSError, SyntaxError, ValueError):
        return None


def _collect_metadata(root: Path) -> list[dict[str, str]]:
    return [
        {**frontmatter, "__file__": str(path)}
        for path in root.rglob("*.py")
        if path.name != "__init__.py"
        if (frontmatter := _extract_frontmatter(path)) is not None
    ]


def _build_toc(entries: list[dict[str, str]]) -> str:
    items: list[str] = []
    for entry in entries:
        date = f' <small>{entry["date"]}</small>' if entry.get("date") else ""
        items.append(
            "<li><a href='{url}'>{title}</a>{date}</li>".format(
                url=entry.get("source_url", "#"),
                title=entry.get("title", entry.get("__file__", "Untitled")),
                date=date,
            )
        )

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def main() -> None:
    root = Path.cwd() / ".." / "proselint" / "checks"
    dist = Path.cwd() / "dist"

    if not root.exists():
        print(f"directory {root} does not exist")
        return

    toc = _build_toc(_collect_metadata(root))

    dist.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "styles.css", "reset.css"):
        _ = copy2(name, dist / name)

    template = Path("rules.html").read_text(encoding="utf-8")
    rules = Template(template).safe_substitute(rules=toc)

    _ = (dist / "rules.html").write_text(rules, encoding="utf-8")


if __name__ == "__main__":
    main()
