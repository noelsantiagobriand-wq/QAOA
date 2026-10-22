import sys
import nbformat

YAML = """\
---
title: QAOA Explorer
description: Solve MaxCut with QAOA on random graphs and compare with classical baselines
show-code: False
format-changelog: True
params:
    n_vertices:
        input: slider
        label: Number of vertices
        min: 4
        max: 14
        value: 8
    edge_prob:
        input: slider
        label: Edge probability
        min: 0.05
        max: 1.0
        step: 0.05
        value: 0.3
    seed:
        input: numeric
        label: Random seed
        value: 67
    p_layers:
        input: slider
        label: QAOA depth (p)
        min: 1
        max: 8
        value: 2
    shots:
        input: select
        label: Number of shots
        choices: [512, 1024, 2048, 4096]
        value: 1024
---
"""


def main(path: str) -> None:
    nb = nbformat.read(path, as_version=4)

    # Remove any previous Mercury header so the script is idempotent
    nb.cells = [c for c in nb.cells if not _is_mercury_cell(c)]

    header = nbformat.v4.new_raw_cell(YAML)
    header["metadata"]["tags"] = ["mercury-params"]
    nb.cells.insert(0, header)

    nbformat.write(nb, path)
    print(f"✅ Mercury header added to {path}")
    print("   Next: replace hardcoded graph/QAOA values in your cells with")
    print("   n_vertices, edge_prob, seed, p_layers, shots.")


def _is_mercury_cell(cell) -> bool:
    return "tags" in cell.get("metadata", {}) and "mercury-params" in cell["metadata"]["tags"]


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "qaoa.ipynb")
