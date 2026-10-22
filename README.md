# QAOA

This is my project for the [TKS](https://www.tks.world/) Build phase: implementing the **Quantum Approximate Optimization Algorithm (QAOA)** to solve combinatorial optimization problems on graphs, built with [Qiskit](https://qiskit.org/) and NetworkX. I have explained it in [this medium blogpost](https://medium.com/@noel.santiago.briand/quantum-optimization-algorithms-03e57f744b12?postPublishedType=initial).

## About
QAOA is a hybrid quantum-classical algorithm that approximates solutions to combinatorial optimization problems such as [MaxCut](https://en.wikipedia.org/wiki/Maximum_cut). This project applies it to randomly generated graphs:
- One type of graph is generated with the [Erdős–Rényi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)
- The second is a constant-[degree](https://en.wikipedia.org/wiki/Degree_(graph_theory)) graph.
- The final type is a [cycle](https://en.wikipedia.org/wiki/Cycle_graph) with [chords](https://en.wikipedia.org/wiki/Chordal_graph).
- 
## How It Works

1. **Graph generation** builds and visualizes a random graph:
2. A [**greedy algorithm**](https://en.wikipedia.org/wiki/Greedy_algorithm) is built to solve classically.
3. **QAOA** solves the problem.
   
## Repository Structure

```text
QAOA/
├── qaoa.ipynb        # Main notebook: graph generation, QAOA circuit, optimization
├── requirements.txt # Python dependencies
├── LICENSE           # MIT License
└── README.md         # This file
```

## Requirements

- Python 3.9+
- [Qiskit](https://qiskit.org/) (and Qiskit Aer for simulation)
- NetworkX
- NumPy
- SciPy
- Matplotlib

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/noelsantiagobriand-wq/QAOA.git
cd QAOA
pip install -r requirements.txt
```

Then launch Jupyter:

```bash
jupyter notebook qaoa.ipynb
```

## Usage

Open `qaoa.ipynb` and run the cells top to bottom:
To try different problem instances, simply change the graph parameters and re-run.

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## Acknowledgements

Built as part of the [TKS](https://www.tks.world/) Build phase. Thanks to the TKS community for feedback and support.
