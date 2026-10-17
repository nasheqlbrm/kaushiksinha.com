# kaushiksinha.com

Primary blog repository for [kaushiksinha.com](https://kaushiksinha.com/).

## Current prototype

The repository currently contains a minimal marimo notebook and a Quarto view:

- `analysis.py` — notebook with a slider and dependent calculation.
- `studio/analysis/dashboard/` — marimo Studio Quarto view.
- `posts/` — draft articles.

The project uses a pinned marimo Studio preview wheel because the released package does not yet include the Quarto provider used by this prototype. The wheel URL and hash are recorded in `pyproject.toml` and `uv.lock`.

## Reproduce the prototype

Prerequisites:

- Python 3.12 or newer within the supported range.
- [`uv`](https://docs.astral.sh/uv/).
- [Quarto](https://quarto.org/docs/get-started/).

From a fresh clone:

```bash
cd /absolute/path/to/kaushiksinha.com
uv sync
uv run marimo check analysis.py
uv run marimo-studio starters
uv run marimo edit analysis.py --port 2720
```

Open <http://127.0.0.1:2720> in a browser. The existing `dashboard` view should open with the Quarto presentation. Its `Rounds` slider should update the displayed square; for example, setting it to `36` should display:

```text
The square of 36 is 1296.
```

The `starters` command should report this provider as available:

```text
available 1.10.19 marimo-studio/quarto:default
```

No separate `marimo-studio` checkout, Node.js, pnpm, or Pixi installation is needed for the current prototype. Those tools were needed only while investigating and building the Studio provider before the preview wheel became available.

## Draft article

The setup history and design rationale are in:

`posts/2026-10-17-marimo-studio-quarto/index.qmd`
