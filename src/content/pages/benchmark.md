---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

**Rakuda** is a ranking of Japanese Large Language Models based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese, in the spirit of English-language leaderboards like the [Huggingface one](https://huggingface.co/spaces/HuggingFaceH4/human_eval_llm_leaderboard). For a detailed explanation of how Rakuda works, please check out [accompanying blog post](/blog/rakuda), and for the full code implementation check out the project on [github](https://github.com/yuzu-ai/japanese-llm-ranking).

In brief, we ask the AI Assistants in the ranking to answer a set of 40 open-ended questions in Japanese about Japanese topics, the [Rakuda questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to the best-performing model for Japanese that we have access to, GPT-3.5, and ask it to choose which model gave a better answer. Based on GPT-3.5's preferences, we estimate the underlying Bradley-Terry strength of each model. Bradley-Terry strengths are Bayesian equivalents to Elo scores.

Please contact us if you have any models that you'd like us to add to this ranking. Please also contact us if you have access to GPT-4, HyperCLOVA, or any other restricted-access model that we could add to the ranking.

| Rank | Model | Strength | Win Rate | Stronger than the next model at confidence level  | 
| :--- | :---: | :---: | :---: | :---: |
| 1 | <a target="_blank" href="https://openai.com/" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>GPT-3.5</a> | 2.490 ± 0.19  | 94% | 100.0%
| 2 | <a target="_blank" href="https://huggingface.co/cyberagent/open-calm-7b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>cyberagent/open-calm-7b</a> | -0.064 ± 0.10  | 52% | 98.6%
| 3 | <a target="_blank" href="https://huggingface.co/izumi-lab/stormy-7b-10ep" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>izumi-lab/stormy-7b-10ep</a> | -0.384 ± 0.10  | 44% | 91.1%
| 4 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b-instruction-ppo</a> | -0.577 ± 0.10  | 39% | 83.7%
| 5 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b-instruction-sft-v2</a> | -0.718 ± 0.10  | 36% | 58.9%
| 6 | <a target="_blank" href="https://huggingface.co/rinna/japanese-gpt-neox-3.6b" style={{color: "var(--link-text-color)", textDecoration: "underline",textDecorationStyle: "dotted"}}>rinna/japanese-gpt-neox-3.6b</a> | -0.751 ± 0.10  | 35% | N/A


![Bradley-Terry strengths of AI assistants on the Rakuda benchmark](/images/blog/rakuda/rakuda_v1ranking.png) 
![Win rates of AI assistants on the Rakuda benchmark](/images/blog/rakuda/rakuda_v1winrate.png)

Date Updated: 2023-06-28