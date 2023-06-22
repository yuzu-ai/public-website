import os
import json
from datetime import datetime



def model_hyperlink(link, model_name):
    return f'<a target="_blank" href="{link}" style="color: var(--link-text-color); text-decoration: underline;text-decoration-style: dotted;">{model_name}</a>'


def make_clickable_model(model_name):
    link = f"https://huggingface.co/{model_name}"


    # Can also hardcode urls and names here here
    # if model_name == "HuggingFaceH4/stable-vicuna-13b-2904":
    #     link = VICUNA_LINK
    #     model_name = "stable-vicuna-13b"
    # elif model_name == "HuggingFaceH4/llama-7b-ift-alpaca":
    #     link = ALPACA_LINK
    #     model_name = "alpaca-13b"
    # if model_name == "dolly-12b":
    #     link = DOLLY_LINK
    # elif model_name == "vicuna-13b":
    #     link = VICUNA_LINK
    # elif model_name == "koala-13b":
    #     link = KOALA_LINK
    # elif model_name == "oasst-12b":
    #     link = OASST_LINK
    # #else:
    # #    link = MODEL_PAGE
  
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
