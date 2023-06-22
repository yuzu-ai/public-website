import os
import json
from datetime import datetime



def model_hyperlink(link, model_name):
    return f'<a target="_blank" href="{link}" style={{{{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}}}>{model_name}</a>'


def make_clickable_model(model_name):
    link = f"https://huggingface.co/{model_name}"


    #Can also hardcode urls and names here
    if 'gpt-3.5-turbo' in model_name:
        link = 'https://openai.com/'
        model_name = "GPT-3.5"

    model_name = model_name.split('/')[-1].replace('-', ' ')

    return model_hyperlink(link, model_name)

def convert_to_markdown(json_file, template_file, markdown_file):
    with open(json_file, "r") as f:
        last_line = f.readlines()[-1]
        data = json.loads(last_line)

    rankings = sorted(data["ranking"], key=lambda x: x["mle"], reverse=True)
    table = "| Rank # | Model | Strength |\n| --- | --- | --- |\n"
    for i, rank in enumerate(rankings):
        table += (
            f"| {i+1} | {make_clickable_model(rank['model_id'])} | {rank['mle']:.3f} |\n"
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
