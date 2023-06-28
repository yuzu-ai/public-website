---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

**Rakuda** is a ranking of Japanese Large Language Models based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese, in the spirit of English-language leaderboards like the [Huggingface one](https://huggingface.co/spaces/HuggingFaceH4/human_eval_llm_leaderboard). For a detailed explanation of how Rakuda works, please check out [accompanying blog post](/blog/rakuda).

In brief, we ask the AI Assistants in the ranking to answer a set of 40 open-ended questions in Japanese about Japanese topics, the [Rakuda questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to the best-performing model for Japanese that we have access to, GPT-3.5, and ask it to choose which model gave a better answer. Based on GPT-3.5's preferences, we estimate the underlying Bradley-Terry strength of each model. Bradley-Terry strengths are Bayesian equivalents to Elo scores.

Please contact us if you have any models that you'd like us to add to this ranking. Please also contact us if you have access to GPT-4, HyperCLOVA, or any other restricted-access model that we could add to the ranking.

$TABLE$

![Bradley-Terry strengths of AI assistants on the Rakuda benchmark]($STRENGTH_CHART$) 
![Win rates of AI assistants on the Rakuda benchmark]($WIN_RATE_CHART$)

Date Updated: $DATE$