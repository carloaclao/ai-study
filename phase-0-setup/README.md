# Phase 0: setup

## Install

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Install a recent NVIDIA driver for your GPU.
3. From the repo root, install the Python packages:

   ```bash
   uv sync
   ```

4. Add PyTorch with CUDA:
   1. Open the install selector at [pytorch.org/get-started](https://pytorch.org/get-started/locally/), pick your OS, "Pip" and the newest CUDA option, and note the tag in the URL it shows (for example `cu128`).
   2. In `pyproject.toml`, uncomment the PyTorch index block and replace `cuXXX` with that tag.
   3. Run:

      ```bash
      uv add torch
      ```

   Do it this way rather than with `uv pip install`: a plain pip install is removed the next time uv syncs the environment, for example whenever you `uv add` another package.

5. Check everything:

   ```bash
   uv run phase-0-setup/check_env.py
   ```

   It should print your GPU's name and finish with "Ready."

## Notebooks

```bash
uv run jupyter lab
```

## Optional

- [LearnHarness](https://learnharness.ai), for Teach and Practice sessions (see "Study method" in AI_ROADMAP.md).
- A [Weights & Biases](https://wandb.ai) account, first used in week 7.
