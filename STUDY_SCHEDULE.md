# Study Schedule: Day by Day

Companion to [AI_ROADMAP.md](AI_ROADMAP.md). The roadmap says *what* to learn and why; this file says *what to do today*.

- **Time:** 1 hour each weekday, 4 hours each weekend day. That is 13 hours a week.
- **Dates:** kickoff weekend Sat Nov 21, 2026, then 40 weeks from Mon Nov 23, 2026 to Sun Aug 29, 2027.
- **Hardware:** an RTX 4070 Ti Super (16 GB) covers everything except the multi-GPU exercise in week 35, which needs two rented GPUs for an afternoon.

## How each week works

| Day | Time | What it's for |
|---|---|---|
| Mon | 1h | 10-minute warm-up (redo anything you missed in last week's Reinforce), then new material |
| Tue to Fri | 1h | New material: one video segment, one paper, or one chapter |
| Sat | 4h | Build: code along, then code it yourself |
| Sun | 3h + 1h | Finish the build, then the **Reinforce** block |

**Weeks 1 to 4 run two tracks.** Weekdays stay on math. Weekends become mostly an **agents side track** (pulled forward from Phase 5), so the math phase isn't math all week:

| Day | Time | What it's for |
|---|---|---|
| Mon to Fri | 1h | Math |
| Sat | 4h | Agents: build |
| Sun | 2h + 1h + 1h | Math lab, then agents, then Reinforce covering both |

Agent work goes in `phase-5-agents/`. The side track needs an API key from a model provider and only basic Python. The tutorials are written in various languages; follow them in Python.

**Reinforce rules.** Do it closed-book first: no notes, no video, no AI. Then check your work. For math, check numerically in NumPy. For explanations, ask a model or a LearnHarness Practice session to grade your answer and find the gap. Anything you miss goes on Monday's warm-up list. Never skip Reinforce to catch up; cut new material instead.

**Falling behind.** Weeks 18 and 36 are buffers. Use them to catch up, or move them to cover travel or a busy stretch at work. If you lose a weekday, fold it into the weekend. If you lose a weekend, slide the week.

**Tracking.** Tick the boxes as you go. Each phase ends with a checkpoint; tick the matching box in the roadmap's progress tracker too.

**Repo layout:**

```
ai-study/
  README.md                 # how to use this repo
  AI_ROADMAP.md             # the syllabus: why, and all the links
  STUDY_SCHEDULE.md         # this file: what to do today
  notes/_template.md        # copy to notes/week-01.md, week-02.md, ...
  phase-0-setup/            # install guide and check_env.py
  phase-1-math/ ... phase-7-capstone/   # your code, one folder per phase
```

---

## Kickoff · Sat Nov 21 – Sun Nov 22 · Re-entry and setup

*Roadmap: Phase 0, 1.1*

- [ ] **Sat Nov 21 · 4h**
  - Setup (1h): push this repo to GitHub, then follow [phase-0-setup/README.md](phase-0-setup/README.md) until `uv run phase-0-setup/check_env.py` prints your GPU and "Ready." Copy `notes/_template.md` to `notes/kickoff.md`.
  - Watch [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), first half (about 1h45m).
  - Read [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) (10 min).
- [ ] **Sun Nov 22 · 4h**
  - Deep Dive, second half (about 1h45m).
  - Rewatch [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) chapters 1 to 3 at 1.5x (45m); it has been a month.
  - Explore [LLM Visualization](https://bbycroft.net/llm) (30m).
  - Reinforce (1h).

**Reinforce**

1. Without notes, write one page on how a chat model is made: tokens, next-token prediction, pretraining data, post-training, and why it hallucinates.
2. Compute by hand, then check in NumPy: 3·(2, 1) + (−1)·(1, 4).
3. Write the matrix for a 90° *clockwise* rotation, using where î and ĵ land.
4. Where does (2, −1) land under the matrix with columns (1, 1) and (−1, 2)?
5. Is (4, 6) in the span of (2, 3) and (−4, −6)? What is that span?
6. Explain why a linear transformation cannot move the origin.

---

# Phase 1: Math refresher (weeks 1 to 4)

## Week 1 · Nov 23 – Nov 29 · Composition, determinants, inverses

*Roadmap 1.1. Series: [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)*

- [ ] **Mon Nov 23 · 1h** — Warm-up. Chapter 4, *Matrix multiplication as composition*: video plus the text lesson and its questions. Compute two compositions by hand and check with `A @ B`.
- [ ] **Tue Nov 24 · 1h** — Chapter 5, *Three-dimensional linear transformations*, and chapter 6, *The determinant*.
- [ ] **Wed Nov 25 · 1h** — Chapter 7, *Inverse matrices, column space and null space*.
- [ ] **Thu Nov 26 · Thanksgiving** — Off. Optional: 15 minutes rereading your week's notes.
- [ ] **Fri Nov 27 · 1h** — Chapter 8, *Nonsquare matrices*. Clone [Tensor Puzzles](https://github.com/srush/Tensor-Puzzles) and do puzzles 1 to 3.
- [ ] **Sat Nov 28 · 4h · Agents: your first agent loop**
  - Read [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) (45m). It explains when to use an agent at all.
  - Get an API key and make one API call that uses a tool, following your provider's tool-use docs (for example Anthropic's [tool use guide](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)) (45m).
  - Follow [How to Build an Agent](https://ampcode.com/how-to-build-an-agent) in Python: a loop with `read_file`, `list_files` and `edit_file` tools (2.5h).
- [ ] **Sun Nov 29 · 4h**
  - Math lab (2h): a grid visualizer in NumPy and matplotlib. Given any 2×2 matrix, draw the original and transformed grid with î and ĵ highlighted. Try a rotation, a shear, a rank-1 matrix, and a matrix with negative determinant. Commit it to `phase-1-math/`.
  - Agents (1h): close the tutorial and rewrite your loop in your own structure.
  - Reinforce (1h).

**Reinforce**

1. Explain why `A @ B` means "apply B first, then A", using where î lands.
2. By hand, then NumPy: the determinant of [[3, 1], [2, 4]]. Does it flip orientation?
3. Multiply a 90° rotation by a shear both ways. Show AB ≠ BA and say what each order does to the grid.
4. For [[1, 2], [2, 4]]: the rank, the column space, the null space, and why it has no inverse.
5. A 3×2 matrix: what dimension goes in, what comes out, and what shape is its column space?
6. ML link: a layer maps 768 dimensions to 3,072. What is the shape of W? If W had rank 64, what would that mean for its outputs?
7. Agents: draw your agent loop from memory. What goes into each API call, what comes back when the model wants a tool, who actually runs the tool, and what ends the loop?

## Week 2 · Nov 30 – Dec 6 · Dot products, change of basis, eigenvectors, SVD

*Roadmap 1.1. This week overlaps NVIDIA GTC in Washington (Nov 30 to Dec 3), so Monday to Thursday are video-only: each 3Blue1Brown chapter is about 15 minutes, which fits a train ride or an evening at the hotel. Skip any day you can't fit and catch up on Friday.*

- [ ] **Mon Nov 30 · 15m (GTC)** — Optional. Chapter 9 video, *Dot products and duality*.
- [ ] **Tue Dec 1 · 15m (GTC)** — Chapter 13 video, *Change of basis*. Think back to our b₁ = (2, 1), b₂ = (−1, 1) example.
- [ ] **Wed Dec 2 · 15m (GTC)** — Chapter 14 video, *Eigenvectors and eigenvalues*.
- [ ] **Thu Dec 3 · 15m (GTC)** — Chapter 15 video, *A quick trick for computing eigenvalues*.
- [ ] **Fri Dec 4 · 1h** — Catch up on any videos you missed, then work the questions in the text lessons for chapters 9, 13 and 14. Skim chapters 10 and 16 if time is left.
- [ ] **Sat Dec 5 · 4h · Agents: tools and a sandbox**
  - Read [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (45m).
  - Add a shell tool that can only run inside a sandbox: a Docker container, or a scratch directory with an allowlist of commands (1.5h).
  - Add a code search tool, for example one that wraps `rg` (45m).
  - Run the agent on 5 small coding tasks and save each conversation as a JSON trace in `phase-5-agents/traces/` (1h).
- [ ] **Sun Dec 6 · 4h**
  - Math lab (2h): watch the first hour of the SVD lecture in [MIT 18.065](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/) (1h). Then compress a grayscale photo with SVD, keeping the top k singular values, and plot the reconstruction error against k (1h).
  - Agents (1h): skim [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) and note which factors your agent breaks.
  - Reinforce (1h).

**At GTC:** if you can pick sessions, CUDA, inference and agent talks will connect directly to Phases 4 to 6. Write down anything you don't understand in this week's note; most of it will make sense by summer.

**Reinforce**

1. Explain the dot product geometrically, then explain why a large dot product between two embeddings means "similar".
2. Take (3, 2) in the basis b₁ = (2, 1), b₂ = (−1, 1). Convert it to standard coordinates and back. Write both change-of-basis matrices.
3. By hand: eigenvalues and eigenvectors of [[3, 1], [0, 2]]. Check in NumPy.
4. From your SVD lab: what k keeps 90% of the energy? In one paragraph, explain why LoRA (Phase 4) is a bet that weight updates are low-rank.
5. Agents: pick one tool your agent misused in its traces. Rewrite its description and say what you changed and why.
6. Agents: what stops your shell tool from touching files outside the sandbox? Try to break it.

## Week 3 · Dec 7 – Dec 13 · Calculus and matrix calculus

*Roadmap 1.2*

- [ ] **Mon Dec 7 · 1h** — Warm-up. [Essence of Calculus](https://www.3blue1brown.com/topics/calculus) chapters 1 to 3.
- [ ] **Tue Dec 8 · 1h** — Chapter 4, *Visualizing the chain rule and product rule*, and chapter 5 on eˣ.
- [ ] **Wed Dec 9 · 1h** — Partial derivatives and the gradient: the first units of [Khan Academy Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus).
- [ ] **Thu Dec 10 · 1h** — [The Matrix Calculus You Need for Deep Learning](https://arxiv.org/abs/1802.01528), through the section on Jacobians.
- [ ] **Fri Dec 11 · 1h** — Same paper: element-wise operations and the vector chain rule.
- [ ] **Sat Dec 12 · 4h · Agents: your first MCP server**
  - Read the [Model Context Protocol](https://modelcontextprotocol.io/) docs on architecture and server primitives, from the current spec (1h).
  - Build an MCP server with two tools over something work-shaped, using fake data (for example a status lookup and a configuration query), with the official Python SDK (2h).
  - Connect it to your agent, and to an existing MCP client such as Claude Code, and compare how each uses it (1h).
- [ ] **Sun Dec 13 · 4h**
  - Math lab (2h): write `numerical_grad(f, x)` using central differences (30m). By hand, derive the gradient of mean squared error for linear regression with respect to w and b, and of cross-entropy for logistic regression, then check both with `numerical_grad` (1.5h).
  - Agents (1h): read [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  - Reinforce (1h).

**Reinforce**

1. Differentiate sin(x²)·eˣ and check numerically at three points.
2. Show that the derivative of the sigmoid is σ(z)(1 − σ(z)).
3. Explain why the Jacobian of f(x) = Wx is W, using the column picture from week 1.
4. Show that the gradient of cross-entropy loss with respect to the softmax inputs is p − y. Verify numerically.
5. In three sentences, explain "backpropagation is the chain rule".
6. Agents: name the MCP server primitives and give one use for each. Why would you put a capability behind MCP instead of hard-coding it as a tool?

## Week 4 · Dec 14 – Dec 20 · Probability, information theory, optimization

*Roadmap 1.3 to 1.5, plus the Phase 1 project*

- [ ] **Mon Dec 14 · 1h** — Warm-up. [Seeing Theory](https://seeing-theory.brown.edu/) chapters 1 and 2: basic and compound probability.
- [ ] **Tue Dec 15 · 1h** — Seeing Theory chapter 3: distributions, expectation, variance.
- [ ] **Wed Dec 16 · 1h** — Seeing Theory chapters 4 and 5: maximum likelihood and Bayesian inference.
- [ ] **Thu Dec 17 · 1h** — [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) (Olah), full read.
- [ ] **Fri Dec 18 · 1h** — [Ruder's gradient descent overview](https://arxiv.org/abs/1609.04747), sections on SGD, momentum and Adam. Play with the demos in [Why Momentum Really Works](https://distill.pub/2017/momentum/).
- [ ] **Sat Dec 19 · 4h · Agents: compaction and your first evals**
  - Add context compaction (summarize old turns when the conversation passes a token budget) and a notes file the agent can write to and read back (2h).
  - Write 10 small tasks, each with an automatic check such as a test that must pass, and run the agent on all of them (1.5h).
  - Read every trace (30m).
- [ ] **Sun Dec 20 · 4h**
  - Math lab (2h): **Phase 1 project**, in NumPy only. Linear regression, both closed-form and gradient descent (1h). Logistic regression on a 2-class toy dataset, plotting the loss and decision boundary (1h). Check every gradient with `numerical_grad`. Stretch, if you have spare time over the holidays: compare SGD, momentum and Adam on the same problem.
  - Agents (1h): error analysis. Sort the failures from yesterday's traces into categories and count them.
  - Reinforce (1h).

**Reinforce**

1. A coin lands heads 7 times in 10. Find the maximum likelihood estimate of p, and show that maximizing likelihood equals minimizing negative log-likelihood.
2. Entropy in bits of a fair coin and of a 90/10 coin.
3. A model predicts [0.7, 0.2, 0.1] and the true class is 0. Compute the cross-entropy, and explain why this is exactly an LLM's loss for one token.
4. Compute KL(p‖q) and KL(q‖p) for p = [0.5, 0.5], q = [0.9, 0.1]. Why do they differ?
5. Why does momentum help in a long, narrow valley? Use the demos in "Why Momentum Really Works" to explain.
6. Agents: list your top three failure types with counts, and the harness change you'd make for each. How many tokens did compaction save, and what did the agent forget?

**Phase 1 checkpoint.** You can read matrix notation and picture the transformation, derive a gradient by hand and check it numerically, and explain cross-entropy. On the agents side, you have a working agent with tools, a sandbox, an MCP server, compaction, and a first set of evals. Tick Phase 1 in the roadmap.

**After week 4** the side track pauses and weekends go back to building for the main phase. Phase 2 is where the math turns into code, so it rarely feels like math. If a later stretch drags, add a side track again: run agents on weekends, or swap one Sunday for [GPU Puzzles](https://github.com/srush/GPU-Puzzles).

---

# Phase 2: ML and deep learning fundamentals (weeks 5 to 9)

## Week 5 · Dec 21 – Dec 27 · Neural network intuition and ML vocabulary

*Roadmap 2.1, 2.2*

- [ ] **Mon Dec 21 · 1h** — Warm-up. [3Blue1Brown Neural Networks](https://www.3blue1brown.com/topics/neural-networks) chapter 1.
- [ ] **Tue Dec 22 · 1h** — Chapter 2, *Gradient descent*.
- [ ] **Wed Dec 23 · 1h** — Chapter 3, *Backpropagation, intuitively*.
- [ ] **Thu Dec 24 · 1h** — Chapter 4, *Backpropagation calculus*.
- [ ] **Fri Dec 25 · Christmas** — Off.
- [ ] **Sat Dec 26 · 4h** — [An Introduction to Statistical Learning](https://www.statlearning.com/) chapter 2, sections 2.1 and 2.2: overfitting, bias and variance, train and test error (1.5h). [Calculus on Computational Graphs](https://colah.github.io/posts/2015-08-Backprop/) (Olah, 45m). On paper: forward and backward pass through a 2-layer network with 2 inputs, 2 hidden units, 1 output (1.75h).
- [ ] **Sun Dec 27 · 4h** — A 2-layer MLP in plain NumPy with hand-written backprop, trained on the two-moons dataset (3h). Reinforce (1h).

**Reinforce**

1. Define overfitting, train/validation/test splits, and bias versus variance, with one example each.
2. Check your paper backward pass from Saturday against `numerical_grad`.
3. Why does a network need a nonlinearity? Answer with week 1: what is the composition of two linear maps?
4. Initialize all weights in your NumPy MLP to zero and train. What happens, and why?

## Week 6 · Dec 28 – Jan 3 · micrograd

*Roadmap 2.2. Video: [The spelled-out intro to neural networks and backpropagation: building micrograd](https://karpathy.ai/zero-to-hero.html) (2h25m)*

- [ ] **Mon Dec 28 · 1h** — Warm-up. micrograd video 0:00 to 0:50: derivatives and the `Value` object.
- [ ] **Tue Dec 29 · 1h** — 0:50 to 1:30: manual backpropagation.
- [ ] **Wed Dec 30 · 1h** — 1:30 to 2:00: implementing `backward()` with topological sort.
- [ ] **Thu Dec 31 · 1h** — 2:00 to end: neurons, MLP, training loop, comparison with PyTorch.
- [ ] **Fri Jan 1 · New Year's Day** — Off.
- [ ] **Sat Jan 2 · 4h** — **Phase 2 project, part 1:** write micrograd from an empty file without looking (3h). Only then compare with [Karpathy's micrograd](https://github.com/karpathy/micrograd) (1h).
- [ ] **Sun Jan 3 · 4h** — Train an MLP with your micrograd on two-moons and plot the decision boundary (2h). Read [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) (1h). Reinforce (1h).

**Reinforce**

1. Why must `backward()` visit nodes in topological order?
2. Why do gradients accumulate with `+=`? Build a case like `a = b + b` that breaks with `=`.
3. Remove `zero_grad` from your training loop. Describe the symptom and explain it.
4. Add `exp` and `pow` to your engine with their backward passes, and test against PyTorch.

## Week 7 · Jan 4 – Jan 10 · makemore 1 and 2: bigram and MLP language models

*Roadmap 2.2. Videos: makemore parts 1 (1h57m) and 2 (1h15m) on the [Zero to Hero page](https://karpathy.ai/zero-to-hero.html)*

- [ ] **Mon Jan 4 · 1h** — Warm-up. makemore part 1, 0:00 to 1:00: bigram counts and sampling.
- [ ] **Tue Jan 5 · 1h** — Part 1, 1:00 to end: negative log-likelihood and the neural bigram model.
- [ ] **Wed Jan 6 · 1h** — [A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) (Bengio et al., 2003), first pass.
- [ ] **Thu Jan 7 · 1h** — makemore part 2, 0:00 to 0:40.
- [ ] **Fri Jan 8 · 1h** — Part 2, 0:40 to end.
- [ ] **Sat Jan 9 · 4h** — Rebuild parts 1 and 2 in your own notebook on a dataset you pick (city names, product names, anything list-like).
- [ ] **Sun Jan 10 · 4h** — Experiments: embedding size, hidden size, a learning-rate finder. Log every run to [Weights & Biases](https://docs.wandb.ai/) with a train/validation/test split (3h). Reinforce (1h).

**Reinforce**

1. Why is the loss of a uniform model over 27 characters ln 27 ≈ 3.30? Use it as your baseline.
2. In linear algebra terms, what does the embedding table do? (Hint: a one-hot vector times a matrix.)
3. Explain your learning-rate-finder plot and where you picked the rate.
4. Compare your train and validation losses. What does the gap tell you?

## Week 8 · Jan 11 – Jan 17 · Activations, BatchNorm, backprop by hand

*Roadmap 2.3. Videos: makemore parts 3 and 4 (about 1h55m each)*

- [ ] **Mon Jan 11 · 1h** — Warm-up. makemore part 3, 0:00 to 1:00: initialization, saturated tanh, Kaiming init.
- [ ] **Tue Jan 12 · 1h** — Part 3, 1:00 to end: BatchNorm and diagnostic plots.
- [ ] **Wed Jan 13 · 1h** — makemore part 4 ("backprop ninja"), 0:00 to 1:00.
- [ ] **Thu Jan 14 · 1h** — Part 4, 1:00 to end.
- [ ] **Fri Jan 15 · 1h** — First pass of [He initialization](https://arxiv.org/abs/1502.01852) and [Layer Normalization](https://arxiv.org/abs/1607.06450).
- [ ] **Sat Jan 16 · 4h** — Do the backprop ninja exercise yourself: backpropagate by hand through the whole MLP, including BatchNorm and cross-entropy.
- [ ] **Sun Jan 17 · 4h** — Add diagnostics to your model: activation histograms and update-to-data ratios (2h). Read the [CS231n notes](https://cs231n.github.io/) on setting up data and the loss (1h). Reinforce (1h).

**Reinforce**

1. Why does tanh saturate, and why does saturation kill gradients?
2. Explain intuitively why Kaiming initialization uses √(2 / fan_in) for ReLU.
3. Which axis does BatchNorm normalize over, and which does LayerNorm? Why do transformers use LayerNorm?
4. Closed book: write the vectorized backward pass of softmax plus cross-entropy in NumPy.

## Week 9 · Jan 18 – Jan 24 · PyTorch, experiment hygiene, Phase 2 project

*Roadmap 2.3 to 2.6*

- [ ] **Mon Jan 18 · 1h** — Warm-up. makemore part 5 (WaveNet), full video (56m).
- [ ] **Tue Jan 19 · 1h** — [PyTorch internals](https://blog.ezyang.com/2019/05/pytorch-internals/) (Yang), first half.
- [ ] **Wed Jan 20 · 1h** — Second half, then the basics of [einops](https://einops.rocks/).
- [ ] **Thu Jan 21 · 1h** — [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook): the guide for starting a new project.
- [ ] **Fri Jan 22 · 1h** — [Troubleshooting Deep Neural Networks](http://josh-tobin.com/troubleshooting-deep-neural-networks.html) (Tobin), and a first pass of [ResNet](https://arxiv.org/abs/1512.03385).
- [ ] **Sat Jan 23 · 4h** — **Phase 2 project, part 2:** an MLP on a small MNIST subset with your micrograd, and the same network in PyTorch. Start both from identical weights and compare gradients.
- [ ] **Sun Jan 24 · 4h** — A proper PyTorch MNIST run: overfit one batch first, then train with a validation split, fixed seeds, W&B logging, and an SGD versus Adam comparison (3h). Reinforce (1h).

**Reinforce**

1. A contiguous tensor has shape (2, 3, 4). What are its strides? What does `.transpose(0, 2)` change, the strides or the data?
2. List the habits from roadmap section 2.6 and point to evidence in your repo that you followed each one.
3. Explain in two sentences why residual connections help gradients flow.
4. Practice session (LearnHarness or a chat model): mixed problems from weeks 1 to 8, without naming the topic up front.

**Phase 2 checkpoint.** You have written an autograd engine, trained networks in it and in PyTorch, and can debug a run that does not converge.

---

# Phase 3: Transformers and LLMs from scratch (weeks 10 to 17)

## Week 10 · Jan 25 – Jan 31 · The road to attention

*Roadmap 3.1, 3.2*

- [ ] **Mon Jan 25 · 1h** — Warm-up. [The Unreasonable Effectiveness of RNNs](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).
- [ ] **Tue Jan 26 · 1h** — [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).
- [ ] **Wed Jan 27 · 1h** — [word2vec](https://arxiv.org/abs/1301.3781), first pass.
- [ ] **Thu Jan 28 · 1h** — [Bahdanau attention](https://arxiv.org/abs/1409.0473), sections 1 to 3.
- [ ] **Fri Jan 29 · 1h** — [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- [ ] **Sat Jan 30 · 4h** — Read [Attention Is All You Need](https://arxiv.org/abs/1706.03762) with the Illustrated Transformer open beside it (2h). Explore [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (1h). Write scaled dot-product attention in NumPy with a causal mask (1h).
- [ ] **Sun Jan 31 · 4h** — Work through [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) code (3h). Reinforce (1h).

**Reinforce**

1. Why divide by √d_k? Show it numerically: compute dot products of random 512-dimensional vectors and look at their variance.
2. Explain why an attention output is a linear combination of the value vectors, and what the attention weights are in that combination.
3. Write a causal mask. What goes wrong in training without it?
4. Why did RNNs struggle with long-range dependencies and with parallel training?
5. Write out every tensor shape in multi-head attention for B = 2, T = 8, C = 64, and 4 heads.

## Week 11 · Feb 1 – Feb 7 · Build a GPT

*Roadmap 3.2. Video: [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (1h56m)*

- [ ] **Mon Feb 1 · 1h** — Warm-up. Video 0:00 to 0:40.
- [ ] **Tue Feb 2 · 1h** — 0:40 to 1:20.
- [ ] **Wed Feb 3 · 1h** — 1:20 to end.
- [ ] **Thu Feb 4 · 1h** — [GPT in 60 Lines of NumPy](https://jaykmody.com/blog/gpt-from-scratch/).
- [ ] **Fri Feb 5 · 1h** — Revisit [LLM Visualization](https://bbycroft.net/llm) and trace one token through the whole model.
- [ ] **Sat Feb 6 · 4h** — Write a GPT from an empty file without the video and train it on tiny Shakespeare on your GPU.
- [ ] **Sun Feb 7 · 4h** — Compare your model with [nanoGPT](https://github.com/karpathy/nanoGPT)'s `model.py`. Ablations at a fixed budget: remove residual connections, then LayerNorm, then positional embeddings, recording validation loss for each (3h). Reinforce (1h).

**Reinforce**

1. Closed book: draw a pre-norm transformer block with the tensor shape at every step.
2. Count parameters by hand for 6 layers, embedding size 384, vocabulary 65, context 256. Check against `sum(p.numel() for p in model.parameters())`.
3. Which ablation hurt most, and why?
4. Why is the output layer often tied to the token embedding matrix?

## Week 12 · Feb 8 – Feb 14 · Tokenization

*Roadmap 3.3. Video: [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (2h13m)*

- [ ] **Mon Feb 8 · 1h** — Warm-up. Video 0:00 to 0:45.
- [ ] **Tue Feb 9 · 1h** — 0:45 to 1:30.
- [ ] **Wed Feb 10 · 1h** — 1:30 to end.
- [ ] **Thu Feb 11 · 1h** — [BPE for neural machine translation](https://arxiv.org/abs/1508.07909) (Sennrich), first pass.
- [ ] **Fri Feb 12 · 1h** — Read the [minbpe](https://github.com/karpathy/minbpe) code: `basic.py` and `regex.py`.
- [ ] **Sat Feb 13 · 4h** — A BPE trainer from scratch: train a 512-token vocabulary on a text corpus.
- [ ] **Sun Feb 14 · 4h** — Add encode, decode, regex pre-tokenization and special tokens. Compare your token counts with [tiktoken](https://github.com/openai/tiktoken) on the same text (3h). Reinforce (1h).

**Reinforce**

1. Tokenize "strawberry" with tiktoken. Use the result to explain why models miscount letters.
2. Given a merge table of three merges, encode a short string by hand.
3. What does a larger vocabulary do to sequence length, embedding parameters and compute?
4. Why do modern tokenizers start from bytes and not Unicode characters?

## Week 13 · Feb 15 – Feb 21 · CS336 assignment 1: setup and tokenizer

*Roadmap 3, spine. [CS336](https://cs336.stanford.edu/) lectures are on YouTube; assignments at [github.com/stanford-cs336](https://github.com/stanford-cs336). Lectures run about 80 minutes, so each spans two days.*

- [ ] **Mon Feb 15 · 1h** — Warm-up. CS336 lecture 1 (overview and tokenization), first half.
- [ ] **Tue Feb 16 · 1h** — Lecture 1, second half.
- [ ] **Wed Feb 17 · 1h** — Lecture 2 (PyTorch and resource accounting), first half.
- [ ] **Thu Feb 18 · 1h** — Lecture 2, second half.
- [ ] **Fri Feb 19 · 1h** — Read the assignment 1 handout's overview and BPE sections. Clone the repo and run the tests; they should all fail.
- [ ] **Sat Feb 20 · 4h** — Adapt your week 12 BPE trainer to the assignment's interface until its tests pass. Parallelize pre-tokenization.
- [ ] **Sun Feb 21 · 4h** — Tokenizer encode and decode to the tests; train a tokenizer on [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories) (3h). Reinforce (1h).

**Reinforce**

1. FLOPs for multiplying an m×k matrix by a k×n matrix, and why.
2. Estimate the FLOPs to train a 124M-parameter model on 10B tokens using C ≈ 6ND.
3. Memory for parameters, gradients and Adam state in fp32 is about 16 bytes per parameter. Break that down, and compute it for 124M parameters.
4. How long would the run in question 2 take on your GPU at 40% of its peak bf16 throughput? (Look up the peak.)

## Week 14 · Feb 22 – Feb 28 · CS336 assignment 1: the transformer

- [ ] **Mon Feb 22 · 1h** — Warm-up. CS336 lecture on architectures and hyperparameters, first half.
- [ ] **Tue Feb 23 · 1h** — Second half.
- [ ] **Wed Feb 24 · 1h** — First passes of [RMSNorm](https://arxiv.org/abs/1910.07467) and [RoFormer](https://arxiv.org/abs/2104.09864).
- [ ] **Thu Feb 25 · 1h** — [GLU Variants](https://arxiv.org/abs/2002.05202) and [LLaMA](https://arxiv.org/abs/2302.13971) section 2.
- [ ] **Fri Feb 26 · 1h** — Read the handout's transformer section and list the modules you will write.
- [ ] **Sat Feb 27 · 4h** — Linear, Embedding, RMSNorm, SwiGLU, RoPE and attention modules, to the tests.
- [ ] **Sun Feb 28 · 4h** — Transformer block, full language model, softmax and cross-entropy, to the tests (3h). Reinforce (1h).

**Reinforce**

1. Explain RoPE as rotations: pairs of dimensions rotated by an angle proportional to position. Why does the query-key dot product then depend only on relative position?
2. Write the RMSNorm formula and say what it drops compared with LayerNorm.
3. Why does SwiGLU use a hidden size of about 8/3 of the model size instead of 4×? Check by counting parameters.

## Week 15 · Mar 1 – Mar 7 · CS336 assignment 1: training

- [ ] **Mon Mar 1 · 1h** — Warm-up. [AdamW](https://arxiv.org/abs/1711.05101), first pass.
- [ ] **Tue Mar 2 · 1h** — Read the handout's optimizer, schedule and training sections.
- [ ] **Wed Mar 3 · 1h** — CS336 lecture on mixture of experts, first half.
- [ ] **Thu Mar 4 · 1h** — Second half.
- [ ] **Fri Mar 5 · 1h** — Plan the training script: data loader, checkpointing, logging.
- [ ] **Sat Mar 6 · 4h** — AdamW, cosine learning-rate schedule with warmup, gradient clipping, data loader and checkpointing, to the tests.
- [ ] **Sun Mar 7 · 4h** — Train on TinyStories on your GPU, sweep the learning rate, and generate samples (3h). Reinforce (1h).

**Reinforce**

1. What does AdamW change about weight decay compared with Adam, and why does it matter?
2. Plot your learning-rate schedule. On your loss curve, mark the warmup and any spikes, and explain them.
3. What does gradient clipping protect against?
4. Generate from one prompt at temperatures 0.5, 1.0 and 1.5, and with top-p 0.9. Describe the differences.

## Week 16 · Mar 8 – Mar 14 · The GPT lineage, scaling, and making training fast

*Roadmap 3.4, 3.6*

- [ ] **Mon Mar 8 · 1h** — Warm-up. [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf).
- [ ] **Tue Mar 9 · 1h** — [GPT-3](https://arxiv.org/abs/2005.14165), sections 1 and 2.
- [ ] **Wed Mar 10 · 1h** — [Scaling Laws](https://arxiv.org/abs/2001.08361) (Kaplan), first pass.
- [ ] **Thu Mar 11 · 1h** — [Chinchilla](https://arxiv.org/abs/2203.15556), first pass.
- [ ] **Fri Mar 12 · 1h** — [BERT](https://arxiv.org/abs/1810.04805), first pass, for contrast.
- [ ] **Sat Mar 13 · 4h** — Watch and code along with [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) (4h), as far as your GPU allows.
- [ ] **Sun Mar 14 · 4h** — Apply its speedups to your assignment 1 model one at a time: TF32, bf16 autocast, `torch.compile`, `F.scaled_dot_product_attention`, and padding the vocabulary to a round number. Measure tokens per second after each (3h). Reinforce (1h).

**Reinforce**

1. Chinchilla: with a budget of 10²¹ FLOPs, C ≈ 6ND and D ≈ 20N, find the compute-optimal N and D.
2. Make a table of each speedup and its gain. Explain the biggest one.
3. Why is BERT not a text generator?
4. What changed between GPT-2 and GPT-3 besides size?

## Week 17 · Mar 15 – Mar 21 · Modern architectures, data, Phase 3 project

*Roadmap 3.5, 3.8*

- [ ] **Mon Mar 15 · 1h** — Warm-up. [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison), first half.
- [ ] **Tue Mar 16 · 1h** — Second half.
- [ ] **Wed Mar 17 · 1h** — [GQA](https://arxiv.org/abs/2305.13245), and the multi-head latent attention section of [DeepSeek-V2](https://arxiv.org/abs/2405.04434).
- [ ] **Thu Mar 18 · 1h** — [DeepSeekMoE](https://arxiv.org/abs/2401.06066) first pass, and the [Mamba](https://arxiv.org/abs/2312.00752) introduction.
- [ ] **Fri Mar 19 · 1h** — [The FineWeb Datasets](https://arxiv.org/abs/2406.17557), first pass.
- [ ] **Sat Mar 20 · 4h** — **Phase 3 project:** pick a dataset you care about and build its pipeline with exact-hash deduplication and two or three simple quality filters. Start training.
- [ ] **Sun Mar 21 · 4h** — Modernization ablation at a fixed budget: baseline with learned positions, LayerNorm and GELU, then swap in RoPE, RMSNorm and SwiGLU one at a time. Write up the results (3h). Reinforce (1h).

**Reinforce**

1. KV cache size is 2 × layers × KV heads × head dimension × sequence length × bytes. Compute it for a 32-layer model with 32 heads of dimension 128, at 32K context in bf16. Then compute it with GQA and 8 KV heads.
2. A mixture-of-experts model has 1T total and 32B active parameters. What does each number determine?
3. Why does deduplication matter? What did your filters remove?
4. From the ablation: which change helped most at your scale?

**Phase 3 checkpoint.** You can write a GPT from an empty file and explain every line, and you have trained and modernized one on your own data.

## Week 18 · Mar 22 – Mar 28 · Buffer and review

Catch up on anything unfinished first. If you're caught up:

- [ ] **Mon to Fri · 1h each** — One Practice session per day on earlier material: linear algebra; calculus and probability; backpropagation; attention; tokenization and training.
- [ ] **Sat Mar 27 · 4h** — Write and publish a post or README about your Phase 3 project: what you built, what you measured, what surprised you.
- [ ] **Sun Mar 28 · 4h** — Reread "Choosing a direction" in the roadmap and decide which sections of Phases 4 to 6 to weight (1h). Fix weak spots from the week (2h). Reinforce (1h).

**Reinforce: mixed exam, closed book**

1. What does `W @ x` compute, geometrically?
2. Gradient of cross-entropy with respect to the logits.
3. Why √d_k in attention?
4. What is in the KV cache, and why does it grow?
5. Why bytes as the tokenizer's base?
6. C ≈ 6ND: what are C, N and D?
7. Why does training need warmup?
8. Residual connections: what problem do they solve?

---

# Phase 4: The modern LLM lifecycle (weeks 19 to 23)

## Week 19 · Mar 29 – Apr 4 · Fine-tuning and post-training

*Roadmap 4.1, 4.2*

- [ ] **Mon Mar 29 · 1h** — Warm-up. [LoRA](https://arxiv.org/abs/2106.09685), sections 1 to 4.
- [ ] **Tue Mar 30 · 1h** — [QLoRA](https://arxiv.org/abs/2305.14314), first pass.
- [ ] **Wed Mar 31 · 1h** — [InstructGPT](https://arxiv.org/abs/2203.02155), first pass.
- [ ] **Thu Apr 1 · 1h** — [DPO](https://arxiv.org/abs/2305.18290), focusing on the loss.
- [ ] **Fri Apr 2 · 1h** — [Constitutional AI](https://arxiv.org/abs/2212.08073), first pass.
- [ ] **Sat Apr 3 · 4h** — Write LoRA yourself: wrap `nn.Linear` with low-rank matrices A and B, apply it to your Phase 3 model, and fine-tune on a new small dataset. Compare trainable parameter counts.
- [ ] **Sun Apr 4 · 4h** — Supervised fine-tuning of a small open model (0.5B to 1.5B parameters) with QLoRA using [PEFT](https://huggingface.co/docs/peft) and [TRL](https://huggingface.co/docs/trl), within your 16 GB (3h). Reinforce (1h).

**Reinforce**

1. LoRA parameter count for a 4096×4096 weight at rank 8, against full fine-tuning.
2. Why is LoRA's B matrix initialized to zero?
3. Explain the DPO loss in plain words.
4. Name the four models in classic RLHF and the job of each.
5. Connect LoRA back to your week 2 SVD lab.

## Week 20 · Apr 5 – Apr 11 · Reasoning models and RL with verifiable rewards

*Roadmap 4.3*

- [ ] **Mon Apr 5 · 1h** — Warm-up. [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903), and the GRPO section of [DeepSeekMath](https://arxiv.org/abs/2402.03300).
- [ ] **Tue Apr 6 · 1h** — The RLVR section of [Tulu 3](https://arxiv.org/abs/2411.15124).
- [ ] **Wed Apr 7 · 1h** — [DeepSeek-R1](https://arxiv.org/abs/2501.12948), sections 1 and 2.
- [ ] **Thu Apr 8 · 1h** — The rest of R1, then the key fixes in [DAPO](https://arxiv.org/abs/2503.14476).
- [ ] **Fri Apr 9 · 1h** — [How frontier models train on outcomes in 2026](https://huggingface.co/blog/sergiopaniego/agentic-rl-2026).
- [ ] **Sat Apr 10 · 4h** — GRPO on a small model (about 0.5B) with [GSM8K](https://huggingface.co/datasets/openai/gsm8k) problems, where the reward is whether the final number is correct. Use TRL's GRPO trainer, or write the loss yourself if you are ahead.
- [ ] **Sun Apr 11 · 4h** — Run training and log accuracy, mean response length, and the spread of rewards within each group. Read some outputs and look for reward hacking (3h). Reinforce (1h).

**Reinforce**

1. A group's rewards are [1, 0, 0, 1]. Compute each GRPO advantage.
2. Why does GRPO not need a critic?
3. What happens to the learning signal when every answer in a group gets the same reward? How does DAPO deal with it?
4. When would you use RLVR, and when RLHF?
5. What did response length do during your training run, and why?

## Week 21 · Apr 12 – Apr 18 · Inference and serving

*Roadmap 4.4*

- [ ] **Mon Apr 12 · 1h** — Warm-up. [Nucleus sampling](https://arxiv.org/abs/1904.09751), sections 1 to 3.
- [ ] **Tue Apr 13 · 1h** — [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) (Weng), first half.
- [ ] **Wed Apr 14 · 1h** — Second half.
- [ ] **Thu Apr 15 · 1h** — [A Visual Guide to Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization).
- [ ] **Fri Apr 16 · 1h** — [Speculative decoding](https://arxiv.org/abs/2211.17192), and [PagedAttention](https://arxiv.org/abs/2309.06180) sections 1 to 3.
- [ ] **Sat Apr 17 · 4h** — Add a KV cache to your Phase 3 model's generation loop. Measure tokens per second with and without it at several sequence lengths.
- [ ] **Sun Apr 18 · 4h** — Run a model in [llama.cpp](https://github.com/ggml-org/llama.cpp) at Q4, Q8 and F16, measuring speed, memory and perplexity. Then measure [vLLM](https://github.com/vllm-project/vllm) throughput under concurrent requests (3h). Reinforce (1h).

**Reinforce**

1. Prefill versus decode: which is compute-bound and which memory-bound, and why?
2. Estimate the decode ceiling as memory bandwidth ÷ model size in bytes. Look up your GPU's bandwidth and do it for a 7B model at 4-bit. Compare with what you measured.
3. Explain PagedAttention by analogy to virtual memory in an operating system.
4. Write top-p sampling from raw logits.

## Week 22 · Apr 19 – Apr 25 · Evaluation, cost and latency

*Roadmap 4.5, 4.8*

- [ ] **Mon Apr 19 · 1h** — Warm-up. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/).
- [ ] **Tue Apr 20 · 1h** — [SWE-bench](https://arxiv.org/abs/2310.06770), first pass.
- [ ] **Wed Apr 21 · 1h** — [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499), first pass.
- [ ] **Thu Apr 22 · 1h** — [LLM Inference Benchmarking: Fundamental Concepts](https://developer.nvidia.com/blog/llm-benchmarking-fundamental-concepts/).
- [ ] **Fri Apr 23 · 1h** — Anthropic's [prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) and [batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) docs, and the [FrugalGPT](https://arxiv.org/abs/2305.05176) and [RouteLLM](https://arxiv.org/abs/2406.18665) abstracts.
- [ ] **Sat Apr 24 · 4h** — The cost exercise from roadmap 4.8. Write a script that measures time to first token and tokens per second for one API model and your local model on the same prompts.
- [ ] **Sun Apr 25 · 4h** — Measuring reliably: compute bootstrap confidence intervals for an eval score, and work out how many samples you need to detect a 5-point difference (2h). Write up the cost exercise (1h). Reinforce (1h).

**Reinforce**

1. Model A scores 70% and model B 74% on 50 tasks. Is the difference real? Show your work.
2. Using current prices you look up, estimate the daily cost of 1,000 tasks with 20K input and 2K output tokens each, with and without caching on 15K of the input.
3. Why does prompt structure affect cost? Link it to the KV cache.
4. When is self-hosting cheaper than an API, and when not?

## Week 23 · Apr 26 – May 2 · Phase 4 project

*Roadmap Phase 4 project: fine-tune, quantize, serve, evaluate*

- [ ] **Mon Apr 26 · 1h** — Warm-up. Pick the task and the dataset; write down what "better" will mean.
- [ ] **Tue Apr 27 · 1h** — Build the eval set: at least 100 examples, with an automatic scorer.
- [ ] **Wed Apr 28 · 1h** — Measure the base model on it. This is your baseline.
- [ ] **Thu Apr 29 · 1h** — Write the LoRA training config.
- [ ] **Fri Apr 30 · 1h** — Plan quantization and serving.
- [ ] **Sat May 1 · 4h** — Fine-tune and evaluate.
- [ ] **Sun May 2 · 4h** — Quantize, serve with llama.cpp or vLLM, and evaluate the quantized model (3h). Reinforce (1h).

**Reinforce**

1. Write up your results with confidence intervals: did fine-tuning help, and did quantization hurt?
2. Read 20 failures and sort them into categories.
3. Explain one thing you would change if you did it again.

**Phase 4 checkpoint.** You can take an open model from download to a served, measured, fine-tuned endpoint, and explain how reasoning models are trained.

---

# Phase 5: Agents, harnesses and loops (weeks 24 to 27)

You built the basic agent in the weeks 1 to 4 side track: the loop, tools, a sandbox, an MCP server, compaction and 10 evals. This phase goes deeper: theory, running it on your own model, cost, harness engineering, retrieval, evals and security.

## Week 24 · May 3 – May 9 · Foundations, and your agent on your own model

*Roadmap 5.0 to 5.2*

- [ ] **Mon May 3 · 1h** — Warm-up. Skim the [prompt engineering overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview); do chapters 1 to 3 of the [interactive tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial).
- [ ] **Tue May 4 · 1h** — [ReAct](https://arxiv.org/abs/2210.03629), first pass.
- [ ] **Wed May 5 · 1h** — [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Weng).
- [ ] **Thu May 6 · 1h** — [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) (OpenAI).
- [ ] **Fri May 7 · 1h** — Reread your December agent code and traces with five months more knowledge. List what you would change.
- [ ] **Sat May 8 · 4h** — Point your agent at a local model served through an OpenAI-compatible endpoint (llama.cpp or vLLM, from week 21). Run your 10 evals against it and against the API model.
- [ ] **Sun May 9 · 4h** — Fix the worst problems from yesterday: tool-call formatting, context length, retries (3h). Reinforce (1h).

**Reinforce**

1. Draw the agent loop, including what ends it.
2. Classify five scenarios of your choosing as "workflow" or "agent", and justify each.
3. Compare the local and API models on your evals. Where did the local model break, and is the cause the model, the context length, or your harness?

## Week 25 · May 10 – May 16 · Context engineering, tools, MCP

*Roadmap 5.3*

- [ ] **Mon May 10 · 1h** — Warm-up. [Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus).
- [ ] **Tue May 11 · 1h** — [Context Rot](https://research.trychroma.com/context-rot).
- [ ] **Wed May 12 · 1h** — Reread [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) with your traces open beside it.
- [ ] **Thu May 13 · 1h** — The [Model Context Protocol](https://modelcontextprotocol.io/) docs: what changed in the spec since December.
- [ ] **Fri May 14 · 1h** — Add per-turn token and cost logging to your agent.
- [ ] **Sat May 15 · 4h** — Make your context cache-friendly: keep the system prompt and tool definitions as a stable prefix, and append instead of rewriting. Measure the cache hit rate and cost per task before and after.
- [ ] **Sun May 16 · 4h** — Harden your MCP server: input validation, clear error messages, and any spec changes from Thursday. Add a third tool (3h). Reinforce (1h).

**Reinforce**

1. Rewrite three deliberately bad tool descriptions so a model would use them correctly.
2. Why should the start of the context stay stable between turns? Link it to the KV cache and caching prices.
3. When is a sub-agent worth its overhead?

## Week 26 · May 17 – May 23 · Harness engineering, multi-agent systems, retrieval

*Roadmap 5.4, 5.5*

- [ ] **Mon May 17 · 1h** — Warm-up. [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) (Hashimoto).
- [ ] **Tue May 18 · 1h** — [Harness Engineering](https://openai.com/index/harness-engineering/) (OpenAI).
- [ ] **Wed May 19 · 1h** — [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system).
- [ ] **Thu May 20 · 1h** — [SWE-agent](https://arxiv.org/abs/2405.15793), first pass.
- [ ] **Fri May 21 · 1h** — [The RAG paper](https://arxiv.org/abs/2005.11401), first pass, and [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval).
- [ ] **Sat May 22 · 4h** — Make your agent read an `AGENTS.md`, add a verification gate (it must run the tests before claiming it is done), and add a search sub-agent.
- [ ] **Sun May 23 · 4h** — A retrieval tool over a folder of docs: BM25 plus embeddings, with contextual prefixes on each chunk. Give it to your agent (3h). Reinforce (1h).

**Reinforce**

1. List five mistakes your agent made this month and the permanent harness fix for each.
2. When does BM25 beat embeddings, and when the reverse?
3. What problem does contextual retrieval solve?

## Week 27 · May 24 – May 30 · Agent evals, security, Phase 5 project

*Roadmap 5.6, 5.7*

- [ ] **Mon May 24 · 1h** — Warm-up. [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
- [ ] **Tue May 25 · 1h** — [Evaluating AI Agents: Moving Past the Vibe Check](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/).
- [ ] **Wed May 26 · 1h** — Selected questions from the [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/).
- [ ] **Thu May 27 · 1h** — [The Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) and two posts from the [prompt injection series](https://simonwillison.net/series/prompt-injection/).
- [ ] **Fri May 28 · 1h** — Skim all ten entries of the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- [ ] **Sat May 29 · 4h** — **Phase 5 project:** run your agent on 20 tasks and read every trace, labeling the failures (2h). Write evals for the most common failure types with [Inspect](https://inspect.aisi.org.uk/) or pytest (2h).
- [ ] **Sun May 30 · 4h** — Improve the harness against the evals. Plant a prompt-injection file in a test repo, see whether your agent follows it, and add a defense (3h). Reinforce (1h).

**Reinforce**

1. Does your agent have all three parts of the lethal trifecta? Which would you remove?
2. Map your agent's risks to three OWASP entries.
3. Report eval scores before and after your changes, with confidence intervals and cost per task.

**Phase 5 checkpoint.** You have a framework-free coding agent with tools, compaction, a sandbox, an eval suite, and at least one security defense.

---

# Phase 6: GPUs and CUDA (weeks 28 to 35)

## Week 28 · May 31 – Jun 6 · C refresher and why GPUs

*Roadmap Phase 6 prerequisite, 6.1*

- [ ] **Mon May 31 · Memorial Day** — Optional: [Beej's Guide to C](https://beej.us/guide/bgc/) chapters on pointers.
- [ ] **Tue Jun 1 · 1h** — Beej: pointers, arrays, and `malloc` and `free`.
- [ ] **Wed Jun 2 · 1h** — Beej: structs, then a minimal Makefile or CMake build.
- [ ] **Thu Jun 3 · 1h** — [Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html).
- [ ] **Fri Jun 4 · 1h** — [The Hardware Lottery](https://arxiv.org/abs/2009.06489), first pass.
- [ ] **Sat Jun 5 · 4h** — C katas: matrix multiplication in C with the naive loop order and then i-k-j. Time both, at `-O0` and `-O3`.
- [ ] **Sun Jun 6 · 4h** — Profile one training step of your Phase 3 model with [torch.profiler](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html). Label each major op compute-bound, memory-bound or overhead-bound (3h). Reinforce (1h).

**Reinforce**

1. Arithmetic intensity (FLOPs per byte moved) of an elementwise add versus a large matmul.
2. Look up your GPU's peak FLOPs and memory bandwidth, and compute the point where an op stops being memory-bound.
3. Why is the i-k-j loop order faster on a CPU?
4. Why does fusing operations help memory-bound code?

## Week 29 · Jun 7 – Jun 13 · Parallel computing and GPU Puzzles

*Roadmap 6.2. [CS149](https://gfxcourses.stanford.edu/cs149) lectures run about 75 minutes; watch the first hour of each.*

- [ ] **Mon Jun 7 · 1h** — Warm-up. CS149: why parallelism, and why efficiency.
- [ ] **Tue Jun 8 · 1h** — CS149: modern multicore processors and SIMD.
- [ ] **Wed Jun 9 · 1h** — CS149: GPU architecture and CUDA, first part.
- [ ] **Thu Jun 10 · 1h** — Same lecture, second part.
- [ ] **Fri Jun 11 · 1h** — *Programming Massively Parallel Processors* (PMPP) chapters 1 and 2, skimmed.
- [ ] **Sat Jun 12 · 4h** — [GPU Puzzles](https://github.com/srush/GPU-Puzzles) 1 to 8.
- [ ] **Sun Jun 13 · 4h** — GPU Puzzles 9 to 14 (3h). Reinforce (1h).

**Reinforce**

1. Explain warps and SIMT, and give a code example of warp divergence.
2. How do GPUs hide memory latency?
3. Redo the puzzle you found hardest from scratch.

## Week 30 · Jun 14 – Jun 20 · First CUDA kernels

*Roadmap 6.3*

- [ ] **Mon Jun 14 · 1h** — Warm-up. Work through [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) and run it.
- [ ] **Tue Jun 15 · 1h** — PMPP chapter 3: multidimensional grids and data.
- [ ] **Wed Jun 16 · 1h** — PMPP chapter 4: compute architecture and scheduling.
- [ ] **Thu Jun 17 · 1h** — [GPU MODE](https://github.com/gpu-mode/lectures) lecture 1: profiling CUDA in PyTorch.
- [ ] **Fri Jun 18 · 1h** — [OLCF CUDA Training](https://www.olcf.ornl.gov/cuda-training-series/) module 1.
- [ ] **Sat Jun 19 · 4h** — Kernels: vector add, SAXPY, ReLU, grayscale and blur on an image. Add an error-checking macro and time kernels with CUDA events.
- [ ] **Sun Jun 20 · 4h** — A naive matmul kernel, checked against `torch.matmul`, and loaded into PyTorch with `torch.utils.cpp_extension.load_inline` (3h). Reinforce (1h).

**Reinforce**

1. Write the index math for a 2D grid of 2D blocks.
2. What happens if you launch more threads than elements and skip the bounds check?
3. Measure host-to-device copy time against kernel time for your vector add. What does that tell you?

## Week 31 · Jun 21 – Jun 27 · Memory hierarchy, coalescing, reductions, tiling

*Roadmap 6.3*

- [ ] **Mon Jun 21 · 1h** — Warm-up. PMPP chapter 5 (memory architecture and data locality), first half.
- [ ] **Tue Jun 22 · 1h** — Chapter 5, second half: tiling.
- [ ] **Wed Jun 23 · 1h** — PMPP chapter 6: performance considerations, especially coalescing.
- [ ] **Thu Jun 24 · 1h** — PMPP chapter on reductions, or the matching GPU MODE lecture.
- [ ] **Fri Jun 25 · 1h** — OLCF module on shared memory.
- [ ] **Sat Jun 26 · 4h** — Reductions three ways (atomics, shared-memory tree, warp shuffle), benchmarked against each other.
- [ ] **Sun Jun 27 · 4h** — Tiled matmul with shared memory, benchmarked against your naive kernel (3h). Reinforce (1h).

**Reinforce**

1. Predict whether coalesced or strided reads are faster and by roughly how much, then measure.
2. What is a shared-memory bank conflict?
3. Show how a tile size of T raises arithmetic intensity, with the formula.

## Week 32 · Jun 28 – Jul 4 · Optimizing matmul with a profiler

*Roadmap 6.4*

- [ ] **Mon Jun 28 · 1h** — Warm-up. [How to Optimize a CUDA Matmul Kernel](https://siboehm.com/articles/22/CUDA-MMM) (Boehm), kernels 1 to 3.
- [ ] **Tue Jun 29 · 1h** — Kernels 4 to 6.
- [ ] **Wed Jun 30 · 1h** — Kernels 7 to 10, reading only.
- [ ] **Thu Jul 1 · 1h** — [Nsight Compute docs](https://docs.nvidia.com/nsight-compute/): getting started and memory workload analysis.
- [ ] **Fri Jul 2 · 1h** — The GPU MODE lecture on the CUDA performance checklist.
- [ ] **Sat Jul 3 · 4h** — Implement Boehm's kernels 1 to 5 yourself and profile each with `ncu`.
- [ ] **Sun Jul 4 · Independence Day** — Light day. Do the Reinforce block (1h) and skip the rest if you want.

**Reinforce**

1. Chart GFLOPs for each of your kernels against cuBLAS.
2. For each step, name the bottleneck the profiler showed.
3. Explain the step that gave the biggest jump.

## Week 33 · Jul 5 – Jul 11 · FlashAttention and Triton

*Roadmap 6.5*

- [ ] **Mon Jul 5 · holiday (observed)** — Optional: [FlashAttention](https://arxiv.org/abs/2205.14135), sections 1 to 3.
- [ ] **Tue Jul 6 · 1h** — Rest of FlashAttention, focusing on the online softmax.
- [ ] **Wed Jul 7 · 1h** — What changed in [FlashAttention-2](https://arxiv.org/abs/2307.08691).
- [ ] **Thu Jul 8 · 1h** — [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html): vector add and fused softmax, reading.
- [ ] **Fri Jul 9 · 1h** — Triton tutorial: matrix multiplication, reading.
- [ ] **Sat Jul 10 · 4h** — Triton fused softmax and matmul, benchmarked against PyTorch.
- [ ] **Sun Jul 11 · 4h** — A Triton FlashAttention forward pass, in the style of CS336 assignment 2 (3h). Reinforce (1h).

**Reinforce**

1. Derive the online softmax update, keeping a running max and running sum.
2. Count reads and writes to GPU main memory for naive attention versus FlashAttention.
3. Why is FlashAttention exact, not an approximation?

## Week 34 · Jul 12 – Jul 18 · cuTile, llm.c, the systems layer

*Roadmap 6.5, 6.6*

- [ ] **Mon Jul 12 · 1h** — Warm-up. The tile programming model in the [CUDA docs](https://docs.nvidia.com/cuda/). Check that cuTile supports your GPU.
- [ ] **Tue Jul 13 · 1h** — [Evaluating CUDA Tile for AI Workloads](https://arxiv.org/abs/2604.23466), first pass.
- [ ] **Wed Jul 14 · 1h** — [llm.c](https://github.com/karpathy/llm.c): read the LayerNorm forward and backward kernels.
- [ ] **Thu Jul 15 · 1h** — llm.c: the attention and matmul kernels.
- [ ] **Fri Jul 16 · 1h** — [Automatic mixed precision](https://pytorch.org/docs/stable/amp.html) and the [torch.compile tutorial](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html).
- [ ] **Sat Jul 17 · 4h** — Port your Triton fused softmax to cuTile if your GPU supports it; otherwise write a fused LayerNorm in Triton. Compare performance and lines of code.
- [ ] **Sun Jul 18 · 4h** — `torch.compile` your Phase 3 model, read the Triton kernels it generates (`TORCH_LOGS=output_code`), and measure the speedup in bf16 (3h). Reinforce (1h).

**Reinforce**

1. Compare hand-written CUDA, Triton and cuTile: what does each hide from you?
2. When is hand-written CUDA still worth it?
3. What did `torch.compile` fuse in your model?

## Week 35 · Jul 19 – Jul 25 · Multi-GPU training and Phase 6 project

*Roadmap 6.6, 6.7*

- [ ] **Mon Jul 19 · 1h** — Warm-up. [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) (Weng).
- [ ] **Tue Jul 20 · 1h** — [PyTorch DDP tutorial series](https://pytorch.org/tutorials/beginner/ddp_series_intro.html), first parts.
- [ ] **Wed Jul 21 · 1h** — DDP series: multi-GPU with `torchrun`.
- [ ] **Thu Jul 22 · 1h** — [ZeRO](https://arxiv.org/abs/1910.02054), first pass.
- [ ] **Fri Jul 23 · 1h** — [Megatron-LM](https://arxiv.org/abs/1909.08053), first pass.
- [ ] **Sat Jul 24 · 4h** — **Phase 6 project:** a custom kernel (fused softmax or attention) for your Phase 3 model, as a PyTorch extension with correctness tests and benchmarks.
- [ ] **Sun Jul 25 · 4h** — Rent two GPUs. Convert your training script to DistributedDataParallel, measure scaling, and profile the all-reduce (3h). Reinforce (1h).

**Reinforce**

1. Why was your two-GPU speedup less than 2×?
2. Memory per GPU for a 1B-parameter model with Adam under plain data parallelism, and under ZeRO stage 3 across two GPUs.
3. When would you choose data, tensor or pipeline parallelism?

**Phase 6 checkpoint.** You have written, profiled and optimized CUDA and Triton kernels, plugged one into your own model, and trained across two GPUs.

## Week 36 · Jul 26 – Aug 1 · Buffer and capstone planning

Catch up first. If you're caught up:

- [ ] **Mon to Wed · 1h each** — Practice sessions mixing all phases.
- [ ] **Thu Jul 29 and Fri Jul 30 · 1h each** — Pick the capstone from roadmap Phase 7, guided by "Choosing a direction".
- [ ] **Sat Jul 31 · 4h** — Publish a write-up of your Phase 6 project.
- [ ] **Sun Aug 1 · 4h** — Write the capstone design doc: goal, scope, how you will measure success, and a milestone for each of the next four weeks (3h). Reinforce (1h): have a model or a friend critique the design doc and revise it.

---

# Phase 7: Capstone (weeks 37 to 40)

The capstone depends on your choice, so the days below are the shape of the work, not specific readings.

## Week 37 · Aug 2 – Aug 8 · Scope, baseline, evals first

- [ ] **Mon to Fri · 1h each** — Mon: set up the repo. Tue: build the eval harness. Wed: get baseline numbers. Thu: read the one paper closest to your project. Fri: refine the plan from what the baseline showed.
- [ ] **Sat Aug 7 · 4h** — Build the core.
- [ ] **Sun Aug 8 · 4h** — Build (3h). Reinforce (1h): explain the design and the baseline to someone, or record a 5-minute walkthrough.

## Week 38 · Aug 9 – Aug 15 · Core build

- [ ] **Mon to Fri · 1h each** — One small, testable piece per day.
- [ ] **Sat Aug 14 · 4h** — Build.
- [ ] **Sun Aug 15 · 4h** — Build (3h). Reinforce (1h): rerun the evals, and write down what changed and why.

## Week 39 · Aug 16 – Aug 22 · Measure, optimize, ablate

- [ ] **Mon to Fri · 1h each** — One measurement or ablation per day.
- [ ] **Sat Aug 21 · 4h** — Optimize the biggest bottleneck.
- [ ] **Sun Aug 22 · 4h** — Final runs (3h). Reinforce (1h): a results table with confidence intervals.

## Week 40 · Aug 23 – Aug 29 · Write up and publish

- [ ] **Mon to Fri · 1h each** — Draft the write-up section by section: problem, approach, results, what failed, what's next.
- [ ] **Sat Aug 28 · 4h** — Clean the repo and finish the README.
- [ ] **Sun Aug 29 · 4h** — Publish (3h). Reinforce (1h): a retrospective on the whole roadmap: what stuck, what didn't, and what to study next. Update AI_ROADMAP.md with it.
