---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

**Rakuda** is a ranking of Japanese Large Language Models based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese, in the spirit of English-language leaderboards like Huggingface's [human_eval_llm](https://huggingface.co/spaces/HuggingFaceH4/human_eval_llm_leaderboard). For a detailed explanation of how Rakuda works, please check out the [accompanying blog post](/blog/rakuda), and for the full code implementation check out the project on [github](https://github.com/yuzu-ai/japanese-llm-ranking).

In brief, we ask the AI Assistants in the ranking to answer a set of [40 open-ended questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to GPT-4 and ask it to choose which model gave a better answer. Based on GPT-4's preferences, we estimate the underlying Bradley-Terry strength of each model in a Bayesian fashion. Bradley-Terry strengths are optimal versions of Elo scores.

Please contact us if you have any suggestions or requests for models that you'd like us to add to this ranking!

| Rank | Model | Strength | Stronger than the next model at confidence level  | 
| :--- | :---: | :---: | :---: |
| 1 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>openai/GPT-4</a> | 1520.915 ± 54.08 | 99.3%
| 2 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>openai/GPT-3.5</a> | 1384.640 ± 44.64 | 100.0%
| 3 | <a target="_blank" href="https://huggingface.co/BlinkDL/rwkv-4-world" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>blinkdl/rwkv-4-world-jp55</a> | 1076.451 ± 34.05 | 91.2%
| 4 | <a target="_blank" href="https://ai-novel.com/index.php" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>ainovelist/supertrin</a> | 1011.049 ± 31.88 | 100.0%
| 5 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b-instruction-ppo</a> | 858.879 ± 33.67 | 61.9%
| 6 | <a target="_blank" href="https://huggingface.co/izumi-lab/stormy-7b-10ep" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>izumi-lab/stormy-7b-10ep</a> | 845.253 ± 32.51 | 76.6%
| 7 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b-instruction-sft-v2</a> | 810.862 ± 33.40 | 65.8%
| 8 | <a target="_blank" href="https://huggingface.co/cyberagent/open-calm-7b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>cyberagent/open-calm-7b</a> | 791.314 ± 32.78 | 97.2%
| 9 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b</a> | 698.791 ± 36.40 | N/A


![Bradley-Terry strengths of AI assistants on the Rakuda benchmark](/images/charts/rakuda_v1_8-10ranking.png) 

Date Updated: 2023-07-14