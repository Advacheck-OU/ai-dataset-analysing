

# Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts
![](https://img.shields.io/badge/Made_with-python-blue.svg)
[![arXiv](https://img.shields.io/badge/arXiv-2410.14677-b31b1b.svg)](https://arxiv.org/abs/2410.14677)
[![LICENSE](https://img.shields.io/badge/License-Apache--2.0-green.svg)](https://github.com/ryuryukke/OUTFOX?tab=Apache-2.0-1-ov-file)



<!-- **Authors:** -->

**_[German Gritsai](https://github.com/grgera)¹ ² , [Anastasia Voznyuk](https://github.com/natriistorm)¹ , [Andrey Grabovoy](https://github.com/andriygav)¹ , Yury Chekhovich¹_**


<!-- **Affiliations:** -->

¹ Advacheck OÜ, Tallinn, Estonia, ² Universite Grenoble Alpes, Grenoble, France,

# :mountain: Overview

The rapid development of autoregressive Large Language Models (LLMs) has significantly improved the quality of generated texts, necessitating reliable machine-generated text detectors. A huge number of detectors and collections with AI fragments have emerged, and several detection methods even showed recognition quality up to 99.9% according to the target metrics in such collections. However, the quality of such detectors tends to drop dramatically in the wild, posing a question: Are detectors actually highly trustworthy or do their high benchmark scores come from the poor quality of evaluation datasets? In this paper, we emphasise the need for robust and qualitative methods for evaluating generated data to be secure against bias and low generalising ability of future model. We present a systematic review of datasets from competitions dedicated to AI-generated content detection and propose methods for evaluating the quality of datasets containing AI-generated fragments. In addition, we discuss the possibility of using high-quality generated data to achieve two goals: improving the training of detection models and improving the training datasets themselves. Our contribution aims to facilitate a better understanding of the dynamics between human and machine text, which will ultimately support the integrity of information in an increasingly automated world.

# :mountain_railway: Analysed Datasets

|           Research Datasets           | Year | Language                           |
|---------------------------------------|------|------------------------------------|                                              
| [GPT-2](https://github.com/openai/gpt-2-output-dataset)              | 2019 | en                                 |
| [TweepFake](https://arxiv.org/abs/2008.00036)        | 2019 | en                                 |
| [HC3](https://arxiv.org/abs/2301.07597)              | 2023 | en, zh                             |
| [GhostBuster](https://arxiv.org/abs/2305.15047)      | 2023 | en                                 |
| [MGTBench](https://arxiv.org/abs/2303.14822)              | 2024 | en                                 |
| [MAGE](https://arxiv.org/abs/2305.13242)             | 2024 | en                                 |
| [M4](https://arxiv.org/abs/2305.14902)               | 2024 | en, zh, ru, bg, ur, id             |
| [OutFox](https://arxiv.org/abs/2307.11729)           | 2024 | en                                 |





| Shared Tasks Datasets           | Year | Language                           |  
|-----------------------------|------|------------------------------------| 
| [DAGPap22](https://www.kaggle.com/competitions/detecting-generated-scientific-papers/)         | 2022 | en                                 |
| [RuATD](https://github.com/dialogue-evaluation/RuATD)            | 2022 | ru                                 |
| [AuTexTification](https://sites.google.com/view/autextification)            | 2023 | en, es                             |
| [IberAuTexTification](https://sites.google.com/view/iberautextification)        | 2024 | es, en, ca, gl, eu, pt             |
| [Voight-Kampff Generative AI (PAN24)](https://pan.webis.de/clef24/pan24-web/generated-content-analysis.html)          | 2024 | en                                 |
| [SemEval 2024 Task 8](https://github.com/mbzuai-nlp/SemEval2024-task8)   | 2024 | en, ar, de, it                     |
| [GenAI Content Detection (MGT-1 Task 1)](https://genai-content-detection.gitlab.io/)      | 2025 | en, zh, it, ar, de, ru, bg, ur, id |



# Citation

If you use that results in your research, please cite our paper:

```bibtex
@misc{2024aidetectorsgoodenough,
      title={Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts}, 
      author={German Gritsai and Anastasia Voznyuk and Andrey Grabovoy and Yury Chekhovich},
      year={2024},
      eprint={2410.14677},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.14677}, 
}
```
