---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

![Chart showing relative strength of models on Rakuda benchmark](/images/charts/rakuda_v1_8-30ranking.png)

**Rakuda** is a ranking of Japanese Large Language Models based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese, in the spirit of English-language leaderboards like Huggingface's [human_eval_llm](https://huggingface.co/spaces/HuggingFaceH4/human_eval_llm_leaderboard). For a detailed explanation of how Rakuda works, please check out the [accompanying blog post](/blog/rakuda), and for the full code implementation check out the project on [github](https://github.com/yuzu-ai/japanese-llm-ranking).

In brief, we ask the AI Assistants in the ranking to answer a set of [40 open-ended questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to GPT-4 and ask it to choose which model gave a better answer. Based on GPT-4's preferences, we estimate the underlying Bradley-Terry strength of each model in a Bayesian fashion. Bradley-Terry strengths are optimal versions of Elo scores.

Please contact us if you have any suggestions or requests for models that you'd like us to add to this ranking!

| Rank | Model | Strength | Stronger than the next model at confidence level  | 
| :--- | :---: | :---: | :---: |
| 1 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>gpt-4</a> | 1526 ± 56 | 100.0%
| 2 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>gpt-3.5</a> | 1339 ± 40 | 100.0%
| 3 | <a target="_blank" href="https://huggingface.co/stabilityai/StableBeluga2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>llama2-70b (StableBeluga2)</a> | 1133 ± 32 | 84.8%
| 4 | <a target="_blank" href="https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>elyza-ja-llama2-7b-fast (instruct)</a> | 1084 ± 34 | 55.4%
| 5 | <a target="_blank" href="https://huggingface.co/NTQAI/chatntq-7b-jpntuned" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rwkv-world-7b (chatntq-jpn)</a> | 1078 ± 34 | 80.4%
| 6 | <a target="_blank" href="https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>elyza-ja-llama2-7b (instruct)</a> | 1038 ± 35 | 61.4%
| 7 | <a target="_blank" href="https://huggingface.co/BlinkDL/rwkv-4-world" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rwkv-world-7b (jp-v1)</a> | 1024 ± 30 | 79.5%
| 8 | <a target="_blank" href="https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>line-3.6b (sft)</a> | 988 ± 32 | 79.9%
| 9 | <a target="_blank" href="https://ai-novel.com/index.php" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>supertrin</a> | 952 ± 28 | 89.6%
| 10 | <a target="_blank" href="https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>ja-stablelm-7b (instruct-alpha)</a> | 900 ± 29 | 95.7%
| 11 | <a target="_blank" href="https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>weblab-10b (SFT)</a> | 820 ± 35 | 96.8%
| 12 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna-3.6b (ppo)</a> | 731 ± 33 | 70.4%
| 13 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna-3.6b (sft)</a> | 706 ± 34 | 70.4%
| 14 | <a target="_blank" href="https://huggingface.co/izumi-lab/stormy-7b-10ep" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>opencalm-7b (stormy)</a> | 680 ± 35 | N/A


Date Updated: 2023-08-30