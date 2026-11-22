# AI Engineering Roadmap: From Math to CUDA

A self-study syllabus for a working software engineer who wants to understand how modern AI works, from the linear algebra up to the GPU kernel.

- **Audience:** software engineer, 5+ years of experience, comfortable in Python, rusty on math
- **Pace:** 10 to 15 hours per week
- **Duration:** about 7 to 9 months end to end (each phase lists its own estimate)
- **Last reviewed:** November 2026 (see the changelog at the end)
- **Day-by-day plan:** [STUDY_SCHEDULE.md](STUDY_SCHEDULE.md), with a weekly Reinforce block

## How to use this syllabus

1. **Build, don't just watch.** Every phase ends with a project. The project is the real curriculum; the readings exist to unblock it.
2. **One primary resource per phase.** Each phase names a *spine* (the one thing to finish). Everything else is supplementary. Skip freely.
3. **Learn math just in time.** Phase 1 is a refresher, not a gate. Spend three to four weeks, move on, and come back when a paper stops making sense.
4. **Keep a repo.** One folder per phase, with notes and code. Writing a short "what I learned" note per week is the best retention tool there is.
5. **Read papers in three passes.** See [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) (Keshav). First pass is five minutes; most papers never need a third.

## Study method: measure, plan, teach, practice

Adapted from [LearnHarness](https://github.com/amosblomqvist/learnharness), an open-source desktop app that uses AI agents to teach. The loop works with the app, with any chat model, or on paper. The roadmap above says *what* to learn; this says *how* to learn each piece so it sticks.

1. **Measure.** Before starting a section, find where your understanding actually ends. Answer a few questions on what the section depends on, and say how confident you are. Start from the first gap, not from page one.
2. **Plan.** Map the dependencies from where you are to the section's goal. If the measure step shows a gap in something earlier (for example, the chain rule before backpropagation), fix that first.
3. **Teach.** Build one reasoning step at a time. For each step, predict the answer before you are told, then check. Repair a confusion before building anything on it. The goal is for the idea to feel obviously true, not just familiar.
4. **Practice.** In a *separate* session, a day or more later, work varied problems that do not name the concept up front. Recognizing which idea a problem needs is the skill that transfers to papers and code.

Two habits carry across all four steps:

- **Think out loud.** Write or dictate your reasoning and uncertainty, not just your answer. A wrong answer with visible reasoning shows exactly what to fix; a bare right answer shows almost nothing.
- **Keep knowledge as claims and chains.** Record what you learned as short claims plus the steps that lead to them ("matrix-vector multiplication is a linear combination of the columns, because each column is where a basis vector lands"). Later sections, and later practice, build on these instead of starting over.

### Where the loop fits

| Material | Teach sessions | Practice sessions | Build |
|---|---|---|---|
| Phase 1 math | Main tool | Main tool | Small NumPy checks |
| Phase 2 to 3 concepts (backprop, attention, tokenization) | Yes | Yes | The phase projects |
| Phase 4 papers (RLVR, inference, quantization) | Yes, with the paper attached | Light | The phase project |
| Phases 5 and 6 (agents, CUDA) | For concepts only (memory hierarchy, eval design) | Light | Mostly building |

The rule of thumb: use the loop for understanding, and the projects for skill. The loop will not replace writing the code.

### Using the LearnHarness app with this roadmap

- **Setup:** install from [learnharness.ai](https://learnharness.ai) (macOS, Windows, Linux). It runs on your own API keys, a Claude Code CLI login, or a local model server; there is no subscription. Sessions and the knowledge graph are stored locally as plain files.
- **One Teach session per subsection.** Name the goal and what you already know, for example: *"Goal: matrix multiplication as composition (3Blue1Brown chapter 4). I understand linear combinations, span, basis, and matrices as transformations."*
- **Attach the source.** Attach the chapter text or the paper PDF so the teaching follows the material in this roadmap.
- **Import your own notes into the graph, not this roadmap.** The roadmap is a list of links; your notes are what the graph is for.
- **Practice weekly from the graph,** mixing earlier phases with the current one, so Phase 1 math stays fresh by Phase 4.

## Roadmap at a glance

| Phase | Topic | Time | Spine resource | Project |
|---|---|---|---|---|
| 0 | Orientation and setup | 1 week | Karpathy, "Deep Dive into LLMs" | Working dev environment |
| 1 | Math refresher | 3 to 4 weeks | 3Blue1Brown + Mathematics for ML | Linear regression from scratch |
| 2 | ML and deep learning fundamentals | 4 to 6 weeks | Karpathy, Zero to Hero (first half) | Autograd engine + MLP |
| 3 | Transformers and LLMs from scratch | 6 to 7 weeks | Zero to Hero (second half) + CS336 | Train your own GPT |
| 4 | The modern LLM lifecycle | 4 weeks | CS336 (later lectures) | Fine-tune and serve a small model |
| 5 | Agents, harnesses, and loops | 4 weeks | Anthropic engineering posts | Coding agent from scratch + evals |
| 6 | GPUs and CUDA | 7 to 8 weeks | GPU MODE lectures + PMPP book | Hand-written CUDA kernels |
| 7 | Capstone | 3+ weeks | Your choice | One deep project |

**Ordering notes:** Phases 5 and 6 are independent of each other. If you get impatient for the hardware side, run Phase 6 in parallel with Phase 5 or swap them. Phase 4 has optional branches (interpretability, multimodal, RL) that you can defer.

## Choosing a direction

"AI-specific role" splits roughly three ways. This roadmap covers all three, so you do not need to choose up front. Revisit this table after Phase 3, when you know which parts you enjoyed, and use it to decide where to go deeper and what to pick for the capstone.

| Direction | What the work is | Sections to weight | Good capstone |
|---|---|---|---|
| Applied AI engineer | Building products and agents on top of models | 4.4, 4.5, 4.8, all of Phase 5 | Agent on your own model |
| Research engineer | Training and improving models | Phases 2 and 3, 2.6, 3.8, 4.1 to 4.3 | Paper reproduction or full-stack tiny LLM |
| Performance and infrastructure | Making training and inference fast and cheap | 4.4, 4.8, all of Phase 6 (especially 6.7) | Inference engine in C++ and CUDA |

---

## Phase 0: Orientation and setup (1 week)

**Goal:** get the big picture so every later detail has somewhere to attach, and get a working environment.

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (Karpathy, 3.5 hours). The best single overview of the whole stack.
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Karpathy, 1 hour). Shorter version if you are pressed for time.
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) (Sutton). One page that explains why the field looks the way it does.
- [LLM Visualization](https://bbycroft.net/llm) (Bycroft). Interactive 3D walk through a GPT forward pass. Revisit it in Phase 3.

**Setup:** Python with `uv` or conda, PyTorch, Jupyter. For GPU access, a free Colab or Kaggle notebook is enough until Phase 3. From Phase 3 onward, budget for occasional cloud GPU rental, or use a local NVIDIA card if you have one (you will want one for Phase 6).

---

## Phase 1: Math refresher (3 to 4 weeks)

**Goal:** rebuild intuition, not rigor. You should finish able to read the notation in a paper and derive a gradient by hand.

**Spine:** the 3Blue1Brown series for intuition, with [Mathematics for Machine Learning](https://mml-book.github.io/) (Deisenroth, Faisal, Ong; free PDF) as the reference text.

### 1.1 Linear algebra (the most important one)

Vectors, matrices as linear maps, dot products, matrix multiplication, rank, eigenvalues, SVD, norms.

- [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) (3Blue1Brown). Start here.
- [MIT 18.06SC Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) (Strang). The classic full course, for depth.
- [MIT 18.065 Matrix Methods in Data Analysis and ML](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/) (Strang). The ML-oriented sequel; sample the SVD and low-rank lectures.
- [Tensor Puzzles](https://github.com/srush/Tensor-Puzzles) (Rush). Broadcasting and tensor thinking as coding puzzles. Very good for engineers.

### 1.2 Calculus and matrix calculus

Derivatives, chain rule, partial derivatives, gradients, Jacobians. The chain rule *is* backpropagation.

- [Essence of Calculus](https://www.3blue1brown.com/topics/calculus) (3Blue1Brown).
- [The Matrix Calculus You Need for Deep Learning](https://arxiv.org/abs/1802.01528) (Parr and Howard). Exactly what the title says.
- [MIT 18.S096 Matrix Calculus for ML and Beyond](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/). Optional depth.

### 1.3 Probability and statistics

Random variables, expectation, variance, conditional probability, Bayes' rule, common distributions, maximum likelihood.

- [Seeing Theory](https://seeing-theory.brown.edu/). Visual, fast refresher.
- [Harvard Stat 110](https://projects.iq.harvard.edu/stat110) (Blitzstein). The full course if you want depth.

### 1.4 Information theory

Entropy, cross-entropy, KL divergence. Cross-entropy is the loss function for every LLM, so this pays off quickly.

- [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) (Olah).

### 1.5 Optimization

Gradient descent, SGD, momentum, adaptive methods.

- [An Overview of Gradient Descent Optimization Algorithms](https://arxiv.org/abs/1609.04747) (Ruder).
- [Why Momentum Really Works](https://distill.pub/2017/momentum/) (Goh, Distill).

**Project:** implement linear and logistic regression in NumPy only. Derive the gradients on paper first, then check them numerically with finite differences.

---

## Phase 2: Machine learning and deep learning fundamentals (4 to 6 weeks)

**Goal:** understand what training a neural network actually is, by building the machinery yourself.

**Spine:** [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) (Karpathy), videos 1 through 5 (micrograd and the makemore series). Type the code yourself.

### 2.1 Classical ML in brief

You do not need a full classical ML course, but you do need the vocabulary: train/validation/test splits, overfitting, bias and variance, regularization, loss functions.

- [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (Ng). Gentle and complete; skim at 1.5x.
- [Stanford CS229](https://cs229.stanford.edu/). The mathematically heavier alternative; the lecture notes are excellent.
- [An Introduction to Statistical Learning](https://www.statlearning.com/) (free PDF). Reference text.

### 2.2 Neural networks and backpropagation

- [Neural Networks](https://www.3blue1brown.com/topics/neural-networks) (3Blue1Brown). Intuition first.
- [micrograd](https://github.com/karpathy/micrograd) (Karpathy). A complete autograd engine in about 150 lines.
- [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) (Olah).
- Paper: [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0) (Rumelhart, Hinton, Williams, 1986).

### 2.3 The craft of training

Initialization, normalization, residual connections, regularization, optimizers, learning rate schedules.

- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) (Karpathy). Read this twice.
- [Stanford CS231n notes](https://cs231n.github.io/). Still the clearest written treatment of the basics.
- Papers (first pass only is fine):
  - [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852) (He initialization)
  - [Batch Normalization](https://arxiv.org/abs/1502.03167) and [Layer Normalization](https://arxiv.org/abs/1607.06450)
  - [Deep Residual Learning](https://arxiv.org/abs/1512.03385) (ResNet). Residual connections are in every transformer.
  - [Dropout](https://jmlr.org/papers/v15/srivastava14a.html)
  - [Adam](https://arxiv.org/abs/1412.6980) and [AdamW](https://arxiv.org/abs/1711.05101)

### 2.4 PyTorch

- [Official PyTorch tutorials](https://pytorch.org/tutorials/).
- [PyTorch internals](https://blog.ezyang.com/2019/05/pytorch-internals/) (Yang). How tensors, strides, and autograd are implemented. Plays to your strengths as an engineer.
- [einops](https://einops.rocks/). Learn it early; it makes tensor code readable.

### 2.5 Reference textbooks (pick one, use as needed)

- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) (Prince, free PDF). Most modern and best illustrated.
- [Dive into Deep Learning](https://d2l.ai/). Code-first.
- [Deep Learning](https://www.deeplearningbook.org/) (Goodfellow, Bengio, Courville). The classic; dated but rigorous.

### 2.6 Experiment hygiene

Tracking runs, making them reproducible, reading loss curves, and debugging a model that will not converge. Neural networks fail silently, so this is the ML equivalent of logging and tests. Set the habits up here, before the expensive runs in Phase 3.

- [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook) (Google Research). A systematic process for hyperparameter tuning and for deciding what to try next.
- [Troubleshooting Deep Neural Networks](http://josh-tobin.com/troubleshooting-deep-neural-networks.html) (Tobin). A decision tree for debugging training.
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/). Course covering the practical side: tooling, experiment management, testing.
- [Weights & Biases documentation](https://docs.wandb.ai/). The most common experiment tracker. Log every run from now on, including the failed ones.
- [Reproducibility](https://pytorch.org/docs/stable/notes/randomness.html) (PyTorch docs). Seeds, determinism, and their limits.

Habits to adopt: overfit a single batch before training on the full dataset, change one thing at a time, keep configs in version control, and write down what you expected before each run.

**Project:** build your own micrograd without looking at the source, train an MLP on MNIST with it, then rewrite the same thing in PyTorch and compare gradients.

---

## Phase 3: Transformers and LLMs from scratch (6 to 7 weeks)

**Goal:** be able to write a GPT from an empty file and explain every line.

**Spine:** the second half of Zero to Hero, then [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/). CS336 is the closest thing to a definitive course on this material: lectures are on YouTube and assignments are public at [github.com/stanford-cs336](https://github.com/stanford-cs336). It is demanding. Doing assignment 1 alone (tokenizer, transformer, optimizer, training loop) is worth more than any amount of reading.

A gentler alternative spine: [Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch) (Raschka), a book with a full companion repo.

### 3.1 The road to attention (history, read quickly)

- [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) (Karpathy)
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) (Olah)
- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) (word2vec)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) (the first attention paper)

### 3.2 The transformer

- Paper: [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Read after the visual explainers, not before.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (Alammar)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) (Harvard NLP). The paper as runnable code.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/). Interactive, runs GPT-2 in the browser.
- [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY) (Karpathy)
- [GPT in 60 Lines of NumPy](https://jaykmody.com/blog/gpt-from-scratch/) (Mody). A good check on your understanding.

### 3.3 Tokenization

- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (Karpathy) and [minbpe](https://github.com/karpathy/minbpe)
- Paper: [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) (BPE)

### 3.4 The GPT lineage

- [BERT](https://arxiv.org/abs/1810.04805) (encoder-only, for contrast)
- [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) (Karpathy). Four hours, covers a real training run including mixed precision and multi-GPU.

### 3.5 What changed in modern architectures

The 2017 transformer is not what ships today. The main deltas:

- Pre-norm with [RMSNorm](https://arxiv.org/abs/1910.07467)
- Rotary position embeddings: [RoFormer](https://arxiv.org/abs/2104.09864)
- SwiGLU activations: [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)
- All of the above assembled: [LLaMA](https://arxiv.org/abs/2302.13971)
- Mixture of experts: [Switch Transformers](https://arxiv.org/abs/2101.03961)
- Survey: [The Transformer Family v2](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) (Weng)

**The 2025 to 2026 deltas.** The dense transformer is being taken apart one layer type at a time, mostly to make inference cheaper. Learn the standard transformer first; these are modifications to it, not replacements for understanding it.

- **Sparse mixture of experts is now the default for large open models.** Each token activates only a small fraction of the parameters. Read [DeepSeekMoE](https://arxiv.org/abs/2401.06066) for the fine-grained expert design most recent models follow.
- **Compressed KV caches.** Multi-head latent attention, introduced in [DeepSeek-V2](https://arxiv.org/abs/2405.04434), projects keys and values into a smaller latent space so long contexts fit in memory. Grouped-query attention ([GQA](https://arxiv.org/abs/2305.13245)) is the simpler predecessor.
- **Hybrid linear attention and state-space layers.** Linear attention and state-space models keep a fixed-size state instead of a cache that grows with the sequence. Recent open models mix many of these linear-time layers with a few full-attention layers. Papers: [Mamba](https://arxiv.org/abs/2312.00752), [Mamba-2 / state space duality](https://arxiv.org/abs/2405.21060), and [Gated Delta Networks](https://arxiv.org/abs/2412.06464). The best mix of layer types is still unsettled.
- **Diffusion decoding** (generating text by refining all positions at once, not left to right) is in small and mid-sized models but unproven at the frontier. Know it exists; don't study it yet.
- Overview: [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) (Raschka). Side-by-side diagrams of recent open-weight architectures. Read it after you have built your own GPT, and the differences will make sense.

### 3.6 Scaling

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (Kaplan et al.)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (Chinchilla)

### 3.7 Reference repos to read

- [nanoGPT](https://github.com/karpathy/nanoGPT). The minimal training codebase.
- [nanochat](https://github.com/karpathy/nanochat). A full ChatGPT-style pipeline (tokenizer, pretraining, fine-tuning, serving) in one small repo.
- Course: [Stanford CS224N](https://web.stanford.edu/class/cs224n/) for broader NLP context.

### 3.8 Data

Collection, filtering, deduplication, and synthetic data. Data quality decides more outcomes than architecture does, and the work is mostly pipeline engineering, so it suits a software background. The CS336 data lectures and assignment 4 cover this hands-on.

- [Common Crawl](https://commoncrawl.org/). The raw web scrape that most pretraining sets start from.
- [The Pile](https://arxiv.org/abs/2101.00027). An early open pretraining dataset, with a clear account of how it was assembled.
- [The FineWeb Datasets](https://arxiv.org/abs/2406.17557). A detailed, modern walkthrough of filtering and deduplicating web data, with ablations for each step. The dataset is on [Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb).
- [TinyStories](https://arxiv.org/abs/2305.07759). A synthetic dataset small enough to train on a single GPU; shows how much data design matters at small scale.
- [Datasheets for Datasets](https://arxiv.org/abs/1803.09010). How to document a dataset.
- [Hugging Face Datasets documentation](https://huggingface.co/docs/datasets). The standard tooling for loading, streaming, and processing.

**Project:** train a small GPT on a dataset you care about (TinyStories, your own code, a book corpus). Write your own BPE tokenizer. Then modernize it: swap in RoPE, RMSNorm, and SwiGLU one at a time and measure the effect on loss. Stretch goal: replace most attention layers with a simple linear-attention layer, keep one or two full-attention layers, and compare loss, speed, and memory at long context lengths.

---

## Phase 4: The modern LLM lifecycle (4 weeks)

**Goal:** understand everything that happens between "a pretrained transformer" and "a product you can call over an API."

**Spine:** the later lectures of CS336 (data, inference, alignment) and the [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) for practical tooling.

### 4.1 Fine-tuning and adaptation

- [LoRA](https://arxiv.org/abs/2106.09685) and [QLoRA](https://arxiv.org/abs/2305.14314). Low-rank adapters; ties directly back to the SVD material in Phase 1.

### 4.2 Post-training: from text predictor to assistant

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) (InstructGPT, the RLHF paper)
- [Proximal Policy Optimization](https://arxiv.org/abs/1707.06347) (PPO, the RL algorithm behind RLHF)
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) (DPO, the simpler alternative)
- [Constitutional AI](https://arxiv.org/abs/2212.08073)
- RL background if you need it: [Spinning Up in Deep RL](https://spinningup.openai.com/) (OpenAI) and [Deep RL: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/) (Karpathy)

### 4.3 Reasoning models and RL with verifiable rewards

This section has grown in importance more than any other. RL with verifiable rewards (RLVR) is now the standard way to train reasoning: instead of a learned reward model, the reward comes from a check you can run, such as whether the math answer is correct or whether the code passes its tests. RLHF is still used for matching human preferences; RLVR is used where correctness can be checked. The newest step is agentic RL, where the model is trained through multi-step tool use inside an environment, which links this section to Phase 5.

- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [DeepSeekMath](https://arxiv.org/abs/2402.03300). Introduces GRPO, the critic-free RL algorithm most open reasoning models are trained with. It samples several answers per prompt and scores each against the group average.
- [Tulu 3](https://arxiv.org/abs/2411.15124). An open post-training recipe that named and described RLVR.
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948). The most detailed public account of training a reasoning model with RL.
- [DAPO](https://arxiv.org/abs/2503.14476). The fixes needed to make GRPO stable at scale; a good look at what goes wrong in practice.
- [How frontier models train on outcomes in 2026](https://huggingface.co/blog/sergiopaniego/agentic-rl-2026) (Hugging Face blog). A map of how recent models combine verifiable rewards, model judges, agentic RL, and distillation.
- [Reinforcement Learning from Human Feedback](https://rlhfbook.com/) (Lambert). Free book covering the whole post-training stack, RLHF through RLVR.
- [Build a Reasoning Model (From Scratch)](https://github.com/rasbt/reasoning-from-scratch) (Raschka)

**Exercise:** train a small open-weights model with GRPO on grade-school math problems, where the reward is simply whether the final number is correct. Watch the average response length and accuracy over training. The CS336 later assignments cover this hands-on.

### 4.4 Inference and serving

Sampling, KV caching, quantization, batching, speculative decoding. This is where a lot of real engineering jobs are.

- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) (nucleus sampling)
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) (Weng)
- [A Visual Guide to Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization) (Grootendorst)
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (the vLLM paper)
- Code to read: [llama.cpp](https://github.com/ggml-org/llama.cpp) and [vLLM](https://github.com/vllm-project/vllm)
- Course: [MIT 6.5940 TinyML and Efficient Deep Learning Computing](https://efficientml.ai/) (Han)

### 4.5 Evaluation

- [SWE-bench](https://arxiv.org/abs/2310.06770). The benchmark that defined coding agent evaluation.
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) (METR)
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) (Husain)

### 4.6 Optional branch: interpretability

What is actually happening inside the model. Fits a curious engineer well, because it is essentially reverse engineering.

- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
- [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- [Getting started in mechanistic interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started) (Nanda)
- [ARENA](https://www.arena.education/). A full hands-on curriculum with exercises.

### 4.7 Optional branch: multimodal and diffusion

Everything so far is text-only. Most frontier models now accept images, and image and video generation runs on a different family of models. A week here is enough to follow the conversation; go deeper if it grabs you.

Vision and multimodal models:

- [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) (ViT). Images as sequences of patches, fed to the transformer you already know.
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) (CLIP). Shared text and image embeddings via contrastive learning.
- [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) (LLaVA). The simplest recipe for connecting a vision encoder to an LLM.
- Course: [Stanford CS231n](https://cs231n.stanford.edu/) for the full computer vision background.

Diffusion models:

- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) (Weng). Start here.
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) (DDPM)
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) (the Stable Diffusion paper)
- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747). The formulation most recent image and video models use.
- [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course). Hands-on notebooks.

### 4.8 Cost and latency

Not optional. These two numbers decide whether a system is viable, and they connect the inference material in 4.4 to the agent work in Phase 5 and the GPU work in Phase 6. Prices change constantly, so learn the structure and look up the current numbers when you need them.

Concepts to know: input versus output token pricing, cached versus uncached input, time to first token versus tokens per second, throughput versus latency under batching, and the cost of a GPU hour versus the cost of an API call for the same work.

Measuring:

- [LLM Inference Benchmarking: Fundamental Concepts](https://developer.nvidia.com/blog/llm-benchmarking-fundamental-concepts/) (NVIDIA). Definitions of the standard metrics and how they trade off.
- [Artificial Analysis](https://artificialanalysis.ai/). Independent, current comparisons of price, speed, and quality across models and providers.
- [LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) (Epoch AI). How fast the cost of a given capability level has been falling, which matters when you plan anything more than a few months out.

Reducing:

- [Prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) and [batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) (Anthropic docs). The two largest levers at the API level. Caching is the KV cache from 4.4 exposed as a pricing feature, which is why prompt structure affects your bill.
- [Latency optimization](https://platform.openai.com/docs/guides/latency-optimization) (OpenAI docs). A general checklist: fewer output tokens, fewer round trips, parallel calls, streaming.
- [FrugalGPT](https://arxiv.org/abs/2305.05176) and [RouteLLM](https://arxiv.org/abs/2406.18665). Cascades and routers: send each request to the cheapest model that can handle it.
- Also relevant: quantization and speculative decoding from 4.4, and the cache-aware context design in the Manus post in 5.3.

**Exercise:** pick a workload (for example, your Phase 5 agent running 1,000 tasks a day). Estimate its monthly cost three ways: a frontier API model, a small API model with caching and batching, and your own quantized model on a rented GPU. Then measure the real numbers and see how far off the estimate was.

**Project:** LoRA fine-tune a small open-weights model on a task of your choice, quantize it, serve it locally with llama.cpp or vLLM, and write a small eval suite that shows whether the fine-tune actually helped.

---

## Phase 5: Agents, harnesses, and loops (4 weeks)

**Goal:** build agents the way you would build any reliable system: small core, good tools, tight feedback loops, measured with evals.

This is the fastest-moving part of the roadmap. The vocabulary has shifted from *prompt engineering* to *context engineering* (what the model sees at each step) to *harness engineering* (the whole environment around the model: tools, memory, constraints, verification). Treat the specific posts below as a snapshot and the principles as durable.

**Spine:** the [Anthropic engineering blog](https://www.anthropic.com/engineering), read in the order listed in 5.2 and 5.3.

### 5.0 Prompting basics (reference)

You likely have most of this from daily use. Skim to fill gaps, then move on; the rest of the phase builds on it.

- [Prompt engineering overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) (Anthropic docs)
- [Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) (OpenAI docs)
- [Prompt engineering interactive tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) (Anthropic). Exercises with answers.
- [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (Weng). The research view: few-shot, chain of thought, and why they work.

### 5.1 Foundations

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629). The origin of the reason-act-observe loop.
- [Toolformer](https://arxiv.org/abs/2302.04761). Early tool use.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Weng). Older but still the best conceptual map.

### 5.2 The agent loop

An agent is a model calling tools in a loop until it decides it is done. Build one before reading too much about them.

- [How to Build an Agent](https://ampcode.com/how-to-build-an-agent) (Ball). A working coding agent in a few hundred lines. Do this first.
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) (Anthropic). Workflows versus agents, and when not to use an agent at all.
- [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) (OpenAI)
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents). Agent design framed as ordinary software engineering principles.

### 5.3 Context engineering and tool design

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic). Compaction, note-taking, sub-agents, just-in-time retrieval.
- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (Anthropic)
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus). Practical, including KV cache considerations that connect back to Phase 4.
- [Context Rot](https://research.trychroma.com/context-rot) (Chroma). Why more context is not always better.
- [Model Context Protocol](https://modelcontextprotocol.io/). The standard interface for tools and data sources. Build one MCP server. The spec revision of July 2026 changed how servers handle state, so work from the current spec, not tutorials written before then.

### 5.4 Harness engineering and multi-agent systems

- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) (Hashimoto). Source of the "engineer the harness" habit: every agent mistake becomes a permanent rule, tool, or check.
- [Harness Engineering](https://openai.com/index/harness-engineering/) (OpenAI)
- [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) (Anthropic)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) (Anthropic)
- [AGENTS.md](https://agents.md/). The cross-tool convention for giving agents project instructions.
- Paper: [SWE-agent](https://arxiv.org/abs/2405.15793). Introduces the idea of the agent-computer interface.

### 5.5 Retrieval

- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (the original RAG paper)
- [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (Anthropic)

### 5.6 Evals for agents

Evals are to agents what tests are to code. Most teams that struggle with agents are missing this piece.

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Anthropic)
- [Evaluating AI Agents: Moving Past the Vibe Check](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) (Google, October 2026). Grade agents with yes/no questions about specific steps, check the sequence of tool calls and not only the final answer, and count time and cost as part of quality.
- [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) (Husain and Shankar)

- [Inspect](https://inspect.aisi.org.uk/). Open-source eval framework from the UK AI Security Institute.

Order of work that has become standard: first read a few dozen agent traces and write down what breaks (error analysis), then write evals only for the failures you actually see.

### 5.7 Security

- [The Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Willison). Private data, untrusted content, and external communication: any agent with all three is exploitable.
- [Prompt injection series](https://simonwillison.net/series/prompt-injection/) (Willison)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). The agent-specific list: goal hijacking through content the agent reads, over-broad tool permissions, memory poisoning, and similar. Built from real incidents. Read this one if you read only one.

### 5.8 Broader practice

- [What We Learned from a Year of Building with LLMs](https://applied-llms.org/)
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) (Huyen). Book-length treatment of the application layer.

**Project:** write a coding agent from scratch with no framework: a loop, three or four tools (read, edit, shell, search), context compaction, and a sandbox. Then build an eval set of 20 small tasks and use it to drive improvements to the harness. Stretch goal: run it against the small model you fine-tuned in Phase 4 and see where it breaks.

---

## Phase 6: GPUs and CUDA (7 to 8 weeks)

**Goal:** understand why deep learning runs on GPUs, write and profile your own kernels, and connect that back to the transformer you built in Phase 3.

**Prerequisite:** working C or C++. If yours is rusty, budget an extra week. You will also need access to an NVIDIA GPU.

C and C++ refresher (CUDA code is mostly C with a little C++, so pointers, memory layout, and the build process matter more than modern C++ features):

- [Beej's Guide to C Programming](https://beej.us/guide/bgc/). Fast and readable; enough for most kernel code.
- [learncpp.com](https://www.learncpp.com/). Free and thorough; use it as a lookup, not a course.
- [A Tour of C++](https://www.stroustrup.com/tour3.html) (Stroustrup). Short book aimed at experienced programmers.

**Spine:** [GPU MODE lectures](https://github.com/gpu-mode/lectures) (a community lecture series that began as a reading group for the textbook below) alongside *Programming Massively Parallel Processors*, 4th edition (Hwu, Kirk, El Hajj), the standard text, usually called PMPP.

### 6.1 Why GPUs

- [Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html) (He). Compute, memory bandwidth, and overhead: the three places time goes. Read this first.
- [The Hardware Lottery](https://arxiv.org/abs/2009.06489) (Hooker). Why the ideas that win are the ones that fit the hardware.
- [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) (AlexNet). The paper that started GPU deep learning.

### 6.2 Parallel computing background

- [Stanford CS149: Parallel Computing](https://gfxcourses.stanford.edu/cs149). Lectures public. Covers parallelism, memory hierarchy, and GPU architecture properly.

### 6.3 CUDA programming

Threads, blocks, and grids; the memory hierarchy (global, shared, registers); coalesced access; reductions; tiling.

- [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) (NVIDIA). Your hello world.
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) (NVIDIA). The official reference.
- [OLCF CUDA Training Series](https://www.olcf.ornl.gov/cuda-training-series/) (Oak Ridge and NVIDIA). Thirteen modules with homework.
- [CUDA course](https://github.com/Infatoshi/cuda-course) (Arledge). A deep learning-oriented course that goes from first kernel to an MLP in raw CUDA, with a matching 12-hour freeCodeCamp video. The same author has a Manning book in early access, *CUDA for Deep Learning*, that extends this to Flash Attention.
- [GPU Puzzles](https://github.com/srush/GPU-Puzzles) (Rush). CUDA concepts as puzzles in Python via Numba. A good on-ramp before C++.

### 6.4 Performance engineering

- [How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance](https://siboehm.com/articles/22/CUDA-MMM) (Boehm). A worked example of iterative kernel optimization. The best single article in this phase.
- [Nsight Compute documentation](https://docs.nvidia.com/nsight-compute/). The profiler. Learn it early; guessing at GPU performance does not work.

### 6.5 Kernels for deep learning

- [FlashAttention](https://arxiv.org/abs/2205.14135) and [FlashAttention-2](https://arxiv.org/abs/2307.08691). The best example of a hardware-aware algorithm that changed practice.
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html). A Python DSL for writing GPU kernels; used in CS336 assignment 2 to implement FlashAttention.
- **CUDA Tile (cuTile).** NVIDIA's own Python DSL for tile-level kernels, stable since CUDA 13.2 (May 2026). Like Triton, you describe operations on blocks of data and the compiler handles threads and Tensor Cores. Start with the [CUDA documentation](https://docs.nvidia.com/cuda/) for the tile programming model, then read [Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/abs/2604.23466), an independent comparison. Its finding: cuTile is very fast on the newest NVIDIA hardware with little code, while Triton is more portable across GPUs.

Recommended order: hand-written CUDA first (6.3 and 6.4), because it teaches what the tile DSLs are hiding. Then Triton. Then cuTile if you work on recent NVIDIA hardware. A recent consumer NVIDIA card (RTX 30 or 40 series) handles everything in this phase except Blackwell-specific features and the multi-GPU project.
- [llm.c](https://github.com/karpathy/llm.c) (Karpathy). GPT-2 training in plain C and CUDA with no framework. Read the CUDA file end to end.
- [tinygrad](https://github.com/tinygrad/tinygrad). A small deep learning framework whose whole stack, down to kernel code generation, is readable.

### 6.6 The systems layer

- [CMU 10-414/714: Deep Learning Systems](https://dlsyscourse.org/). Build your own PyTorch-like framework, including a GPU backend.
- [Automatic Mixed Precision](https://pytorch.org/docs/stable/amp.html) and [torch.compile](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) (PyTorch docs)
- [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) (Weng). Data, model, and pipeline parallelism.
- [Machine Learning Engineering Open Book](https://github.com/stas00/ml-engineering) (Bekman). Field notes on running real training jobs.

### 6.7 Multi-GPU training, hands-on

Reading about distributed training is not the same as debugging it. Rent two GPUs for an afternoon and do this once.

- [Distributed Data Parallel in PyTorch](https://pytorch.org/tutorials/beginner/ddp_series_intro.html) (PyTorch tutorial series). Single GPU to multi-GPU to multi-node, step by step.
- [Hugging Face Accelerate](https://huggingface.co/docs/accelerate). The thin wrapper most people use in practice; read it after doing DDP by hand.
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054). Sharding optimizer state and gradients across devices; the idea behind FSDP.
- [Megatron-LM](https://arxiv.org/abs/1909.08053). Tensor (model) parallelism for transformers.

**Project:** write matrix multiplication in CUDA and optimize it step by step (naive, coalesced, tiled with shared memory), profiling each version with Nsight Compute. Then write a custom kernel for one piece of your Phase 3 model (a fused softmax or attention), expose it to PyTorch as an extension, and benchmark it against the built-in.

**Second project (multi-GPU):** convert your Phase 3 training script to DistributedDataParallel and run it on two GPUs. Measure throughput against one GPU, explain why the speedup is less than 2x, and find the bottleneck with a profiler.

---

## Phase 7: Capstone (3+ weeks)

Pick one project that crosses at least two phases. Some options:

1. **Full-stack tiny LLM.** Tokenizer, pretraining, chat fine-tuning, quantized inference server, and a web UI, all in one repo you wrote. nanochat is the reference point.
2. **Agent on your own model.** Fine-tune a small open-weights model for tool calling and build the harness and evals around it.
3. **Inference engine.** Write a minimal GPT-2 inference engine in C++ and CUDA with KV caching and batching. Benchmark it against llama.cpp.
4. **Paper reproduction.** Pick one paper from this syllabus and reproduce its headline result at small scale.
5. **Interpretability study.** Train a sparse autoencoder on your Phase 3 model and document what features you find.
6. **Kernel-writing agent.** Build an agent that writes a Triton or CUDA kernel, checks it against a PyTorch reference for correctness, profiles it, and iterates. Using LLM agents to generate and optimize GPU kernels is an active research area in 2026, and this project combines Phases 5 and 6 directly. [KernelBench](https://arxiv.org/abs/2502.10517) is a ready-made set of tasks to test against.

Write it up. A clear write-up of a real project is the most useful artifact for moving into an AI-focused role.

---

## What was added beyond the original outline, and why

- **Classical ML basics (2.1).** A short stop, but the vocabulary (overfitting, regularization, validation) is assumed everywhere.
- **Information theory (1.4).** Cross-entropy and KL divergence are the language of LLM training.
- **Post-training and reasoning (4.2, 4.3).** The gap between a pretrained model and an assistant is where much of the current action is.
- **Inference and serving (4.4).** Quantization, KV caching, and batching are the bridge between the model phase and the GPU phase, and a common entry point for software engineers moving into AI roles.
- **Evals (4.5, 5.6).** The single most transferable skill from software engineering, and the thing most often skipped.
- **Agent security (5.7).** Required reading before giving any agent real permissions.
- **Interpretability (4.6).** Optional, included because it suits someone who wants to know how things work.
- **Parallel computing and DL systems (6.2, 6.6).** CUDA makes far more sense with the surrounding context.
- **Experiment hygiene (2.6).** Tracking, reproducibility, and debugging training runs, placed before the expensive runs begin.
- **Data (3.8).** Curation, filtering, and synthetic data; often the highest-leverage work in practice.
- **Multimodal and diffusion (4.7).** Optional branch so the roadmap is not text-only.
- **Cost and latency (4.8).** How to measure and reduce the two numbers that decide whether a system is viable.
- **Prompting basics (5.0).** A short reference before context and harness engineering.
- **C and C++ refresher (Phase 6 prerequisite).**
- **Multi-GPU training, hands-on (6.7).** A real exercise instead of a single reading.
- **Choosing a direction.** A map of the three role types against the phases, to revisit after Phase 3.

## Staying current

The fundamentals in Phases 1 through 3 are stable. Phases 4 through 6 move quickly. A light habit is enough:

- [Simon Willison's blog](https://simonwillison.net/). The most reliable running commentary on applied LLMs.
- [Lilian Weng's blog](https://lilianweng.github.io/). Deep survey posts.
- [Sebastian Raschka's Ahead of AI](https://magazine.sebastianraschka.com/). Research digests with an implementation bent.
- [Anthropic engineering](https://www.anthropic.com/engineering) and [Transformer Circuits](https://transformer-circuits.pub/).
- [arXiv cs.LG](https://arxiv.org/list/cs.LG/recent) and [cs.CL](https://arxiv.org/list/cs.CL/recent), skimmed, not read.

## Changelog

**November 2026 review.** The structure and Phases 0 to 2 are unchanged; new model releases do not change fundamentals. Updates:

- **3.5:** added the 2025 to 2026 architecture changes (sparse mixture of experts, compressed KV caches, hybrid linear-attention and state-space layers) and a stretch goal for the Phase 3 project.
- **4.3:** expanded into RL with verifiable rewards, GRPO, and agentic RL, now the standard way reasoning models are trained, with a hands-on exercise.
- **5.3:** noted the July 2026 MCP spec revision.
- **5.6:** added Google's October 2026 agent evaluation guide and the error-analysis-first workflow.
- **5.7:** added the OWASP Top 10 for Agentic Applications.
- **6.5:** added NVIDIA's CUDA Tile (cuTile) and a recommended learning order across CUDA, Triton, and cuTile.
- **Capstone:** added a kernel-writing agent option.

**November 2026, study method.** Added the measure, plan, teach, practice loop adapted from LearnHarness, with a map of where it fits in each phase and how to use the app with this roadmap.

## Progress tracker

- [ ] Phase 0: Orientation and setup
- [ ] Phase 1: Math refresher (project: regression from scratch)
- [ ] Phase 2: ML and DL fundamentals (project: autograd engine + MLP)
- [ ] Phase 3: Transformers and LLMs (project: train your own GPT)
- [ ] Phase 4: Modern LLM lifecycle (project: fine-tune, quantize, serve, evaluate)
- [ ] Phase 5: Agents and harnesses (project: coding agent + eval suite)
- [ ] Phase 6: GPUs and CUDA (project: optimized kernels + PyTorch extension)
- [ ] Phase 7: Capstone
