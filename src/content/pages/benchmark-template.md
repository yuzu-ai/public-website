---
title: "The Rakuda Ranking of Japanese AI"
meta_title: ""
description: ""
draft: false
---

**Rakuda** is a ranking of Japanese Large Language Models and AI Assistants based on how well they answer a set of open-ended questions in Japanese about Japanese topics. We hope that Rakuda can help stimulate the development of open-source models that perform well in Japanese. For a detailed explanation of how Rakuda works, please check out [accompanying blog post](/blog/rakuda).

In brief, we ask the AI Assistants in the ranking to answer a set of 40 open-ended questions in Japanese about Japanese topics. We call these questions the [Rakuda questions](https://huggingface.co/datasets/yuzuai/rakuda-questions). We then show pairs of these answers to the best-performing model for Japanese that we have access to, GPT-3.5, and ask it to choose which model gave a better answer to the question. Based on GPT-3.5's preferences, we estimate the underlying Bradley-Terry strength of each model. Bradley-Terry strengths are Bayesian equivalents to Elo scores, if you're familiar with that.

Please contact us if you have any models that you'd like us to add to this ranking. Please also contact us if you have access to GPT-4, HyperCLOVA, or any other restricted-access model that we could add to the ranking.

$TABLE$

{/* $WIN_RATE_CHART$ $STRENGTH_CHART$ */}

Date Updated: $DATE$