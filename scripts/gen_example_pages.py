"""Generate Markdown documentation pages for example Python scripts."""

import ast
from pathlib import Path

import mkdocs_gen_files

examples_root = Path("docs/examples")

index_rows: list[str] = []
summary_lines = ["* [Overview](index.md)\n"]

for path in sorted(p for p in examples_root.glob("*.py") if p.stem != "__init__"):
    source = path.read_text()

    try:
        tree = ast.parse(source)
        docstring = ast.get_docstring(tree) or ""
    except SyntaxError:
        docstring = ""

    title = path.stem.replace("_", " ").title()
    first_line = docstring.split("\n")[0].rstrip(".") if docstring else ""

    index_rows.append(f"| [{title}]({path.stem}.md) | {first_line} |")
    summary_lines.append(f"* [{title}]({path.stem}.md)\n")

    lines = [f"# {title}", ""]
    if docstring:
        lines += [docstring, ""]
    lines += [
        "```python",
        source.rstrip(),
        "```",
        "",
    ]

    doc_path = Path("docs/examples") / path.with_suffix(".md").name
    with mkdocs_gen_files.open(doc_path, "w") as f:
        f.write("\n".join(lines))

index_lines = [
    "# Examples",
    "",
    "Ready-to-run code examples covering common use cases.",
    "",
    "| Example | Description |",
    "| --- | --- |",
    *index_rows,
    "",
]

with mkdocs_gen_files.open("docs/examples/index.md", "w") as f:
    f.write("\n".join(index_lines))

with mkdocs_gen_files.open("docs/examples/SUMMARY.md", "w") as f:
    f.writelines(summary_lines)
