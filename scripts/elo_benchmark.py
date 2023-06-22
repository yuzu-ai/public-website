import os
import json
from datetime import datetime


def convert_to_markdown(json_file, template_file, markdown_file):
    with open(json_file, "r") as f:
        last_line = f.readlines()[-1]
        data = json.loads(last_line)

    rankings = sorted(data["ranking"], key=lambda x: x["mle"], reverse=True)
    table = "| Rank # | Model | Strength |\n| --- | --- | --- |\n"
    for i, rank in enumerate(rankings):
        table += (
            f"| {i+1} | {rank['model_id']} | {format(float(rank['mle']), '.5f')} |\n"
        )

    with open(template_file, "r") as f:
        lines = f.readlines()

    lines.pop()
    lines.append(table)

    lines.append("\n")
    lines.append(f"Updated: {datetime.fromisoformat(data['date']).date()}")

    # delete existing markdown_file
    os.remove(markdown_file)

    with open(markdown_file, "w") as file:
        file.writelines(lines)

    print("Converted elo ranking to markdown table")


if __name__ == "__main__":
    convert_to_markdown(
        "./src/content/pages/registry.jsonl",
        "./src/content/pages/benchmark-template.md",
        "./src/content/pages/benchmark.md",
    )
