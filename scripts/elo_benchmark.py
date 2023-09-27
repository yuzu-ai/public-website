import os
import json
from datetime import datetime


def model_hyperlink(link, model_name):
    return f'<a target="_blank" href="{link}" style={{{{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}}}>{model_name}</a>'


def make_clickable_model(model_name, short_name):
    link = f"https://huggingface.co/{model_name}"

    # Can hardcode urls and names here
    link_map = {"gpt-3.5" : "https://openai.com/",
    "gpt-4": "https://openai.com/",
    "claude": "https://anthropic.com",
    "super-trin": "https://ai-novel.com/index.php",
    "rwkv-world-jp": "https://huggingface.co/BlinkDL/rwkv-4-world",
    "stablebeluga": "https://huggingface.co/stabilityai/StableBeluga2",
    "line-3.6b-sft": "https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft",
    "weblab-10b-instruction-sft":"https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft",
    "elyza-7b-fast": "https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct",
    "elyza-7b": "https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct",
    "ja-stablelm-7b": "https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b",
    "rinna-3.6b-ppo": "https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo",
    "rinna-3.6b-sft": "https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2",
    "chatntq-7b-jpntuned": "https://huggingface.co/NTQAI/ChatNTQ_7B_Japanese"}

    for key, link in link_map.items():
        if key in short_name.lower() or key in model_name.lower():
            return model_hyperlink(link, short_name)

    return short_name


def convert_to_markdown(json_file, strength_fig_file, template_file, markdown_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    rankings = sorted(data["ranking"], key=lambda x: x["median"], reverse=True)
    table = "| Rank | Model | Strength | Stronger than the next model at confidence level  | \n| :--- | :---: | :---: | :---: |\n"
    for i, rank in enumerate(rankings):
        # assert(round(rank['one_sigma_up'],2) == round(rank['one_sigma_down'],2))
        table += f"| {i+1} | {make_clickable_model(rank['model_id'], rank['display_name'])} | {rank['median']:.0f} ± {rank['one_sigma_plus']:.0f} | { str(round(rank['stronger_than_next_confidence']*100,1))+'%' if rank['stronger_than_next_confidence']>0 else 'N/A'}\n"

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
        "./src/content/pages/ranking.json",
        "/images/charts/ranking.png",
        "./src/content/pages/benchmark-template.md",
        "./src/content/pages/benchmark.md",
    )
