import os
import json
from datetime import datetime


def model_hyperlink(link, model_name):
    return f'<a target="_blank" href="{link}" style={{{{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}}}>{model_name}</a>'


def make_clickable_model(model_name):
    link = f"https://huggingface.co/{model_name}"

    # Can hardcode urls and names here
    if "gpt-3.5-turbo" in model_name:
        link = "https://openai.com/"
        model_name = "openai/GPT-3.5"
    elif "gpt-4" in model_name:
        link = "https://openai.com/"
        model_name = "openai/GPT-4"
    elif "super-torin" in model_name:
        link = "https://ai-novel.com/index.php"
        model_name = "ainovelist/super-torin"
    elif "rwkv" in model_name:
        link = "https://huggingface.co/BlinkDL/rwkv-4-world"
        model_name = "blinkdl/rwkv-4-world-jp55"

    return model_hyperlink(link, model_name)


def convert_to_markdown(json_file, strength_fig_file, template_file, markdown_file):
    with open(json_file, "r") as f:
        last_line = f.readlines()[-1]
        data = json.loads(last_line)

    rankings = sorted(data["ranking"], key=lambda x: x["median"], reverse=True)
    table = "| Rank | Model | Strength | Stronger than the next model at confidence level  | \n| :--- | :---: | :---: | :---: |\n"
    for i, rank in enumerate(rankings):
        # assert(round(rank['one_sigma_up'],2) == round(rank['one_sigma_down'],2))
        table += f"| {i+1} | {make_clickable_model(rank['model_id'])} | {rank['median']:.3f} ± {rank['one_sigma_up']:.2f} | { str(round(rank['stronger_than_next_confidence']*100,1))+'%' if rank['stronger_than_next_confidence']>0 else 'N/A'}\n"

    with open(template_file, "r") as f:
        template = f.read()

    template = template.replace("$TABLE$", table)

    template = template.replace("$STRENGTH_CHART$", strength_fig_file)

    template = template.replace(
        "$DATE$", str(datetime.fromisoformat(data["date"]).date())
    )

    # delete existing markdown_file
    os.remove(markdown_file)

    with open(markdown_file, "w") as file:
        file.write(template)


if __name__ == "__main__":
    convert_to_markdown(
        "./src/content/pages/registry.jsonl",
        "/images/charts/rakuda_v1_gpt4ranking.png",
        "./src/content/pages/benchmark-template.md",
        "./src/content/pages/benchmark.md",
    )
