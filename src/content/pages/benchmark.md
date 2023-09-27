---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

![Chart showing relative strength of models on Rakuda benchmark](/images/charts/ranking.png)

**Rakuda** is a ranking of Japanese Large Language Models based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese, in the spirit of English-language leaderboards like Huggingface's [human_eval_llm](https://huggingface.co/spaces/HuggingFaceH4/human_eval_llm_leaderboard). For a detailed explanation of how Rakuda works, please check out the [accompanying blog post](/blog/rakuda), and for the full code implementation check out the project on [github](https://github.com/yuzu-ai/japanese-llm-ranking).

In brief, we ask the AI Assistants in the ranking to answer a set of [40 open-ended questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to GPT-4 and ask it to choose which model gave a better answer. Based on GPT-4's preferences, we estimate the underlying Bradley-Terry strength of each model in a Bayesian fashion. Bradley-Terry strengths are optimal versions of Elo scores.

Please contact us if you have any suggestions or requests for models that you'd like us to add to this ranking!

| Rank | Model | Strength | Stronger than the next model at confidence level  | 
| :--- | :---: | :---: | :---: |
| 1 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>gpt-4</a> | 1472 ± 49 | 97.5%
| 2 | <a target="_blank" href="https://anthropic.com" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>claude-2</a> | 1353 ± 42 | 89.3%
| 3 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>gpt-3.5</a> | 1285 ± 37 | 100.0%
| 4 | <a target="_blank" href="https://huggingface.co/stabilityai/StableBeluga2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>llama2-70b (StableBeluga2)</a> | 1089 ± 30 | 85.8%
| 5 | <a target="_blank" href="https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>elyza-7b-fast</a> | 1044 ± 29 | 75.0%
| 6 | <a target="_blank" href="https://huggingface.co/NTQAI/ChatNTQ_7B_Japanese" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>chatntq-7b-jpntuned</a> | 1017 ± 29 | 50.9%
| 7 | <a target="_blank" href="https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>elyza-7b</a> | 1016 ± 29 | 86.8%
| 8 | <a target="_blank" href="https://huggingface.co/BlinkDL/rwkv-4-world" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rwkv-world-7b-jp-v1</a> | 971 ± 29 | 89.8%
| 9 | <a target="_blank" href="https://ai-novel.com/index.php" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>super-trin</a> | 921 ± 27 | 71.4%
| 10 | <a target="_blank" href="https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>line-3.6b</a> | 899 ± 29 | 92.8%
| 11 | <a target="_blank" href="https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>ja-stablelm-7b</a> | 839 ± 28 | 95.3%
| 12 | <a target="_blank" href="https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>weblab-10b</a> | 764 ± 33 | 97.5%
| 13 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna-3.6b (PPO)</a> | 674 ± 36 | 66.2%
| 14 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna-3.6b (SFT)</a> | 653 ± 36 | N/A


Date Updated: 2023-09-27