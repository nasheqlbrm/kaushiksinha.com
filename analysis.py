# /// script
# requires-python = ">=3.10,<3.15"
#
# [tool.marimo-studio]
# default = "dashboard"
#
# [tool.marimo-studio.cells]
# cell-2 = {ref = "cell:v1:fa88d4db3113a5b106cfa75dd1e1b5866e88f7157fd0431ad3a42313208d73dc:cc9d70d69c1c2af52196cbc3f9f2d4b9f67cff41fa5dcd97a8f18ac7558b62ff:0"}
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    rounds = mo.ui.slider(1, 100, value=10, label="Rounds")
    rounds
    return mo, rounds


@app.cell
def _(rounds):
    total = rounds.value**2
    return (total,)


@app.cell
def _(mo, rounds, total):
    mo.md(f"""
    The square of **{rounds.value}** is **{total}**.
    """)
    return


if __name__ == "__main__":
    app.run()
