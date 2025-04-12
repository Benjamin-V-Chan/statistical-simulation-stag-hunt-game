# statistical-simulation-stag-hunt-game

## Project Overview

This project simulates the **Stag Hunt Game**, an evolutionary game-theoretic model of coordination. In this game, two individuals may choose to cooperate (hunt stag) or act selfishly (hunt hare). Cooperation yields higher rewards if both choose to cooperate, but defecting ensures a smaller, safer payoff. This simulation models population-level dynamics over many generations using replicator dynamics, a key mechanism in evolutionary game theory.

### Mathematical Foundations

Let the system evolve over discrete generations indexed by $t \in \{0, 1, \dots, T\}$. Each individual in the population selects a strategy $s_i \in \{\text{stag}, \text{hare}\}$. The payoff structure is symmetric and defined by a matrix:

$$\begin{bmatrix}
    R_{ss} & R_{sh} \\
    R_{hs} & R_{hh}
\end{bmatrix} =
\begin{bmatrix}
    4 & 0 \\
    3 & 2
\end{bmatrix}$$

Let $f_t$ be the fraction of individuals choosing "stag" at generation $t$, and $1 - f_t$ be the fraction choosing "hare". Then the **expected payoff** of each strategy is:

- Stag: $$E_s(f_t) = f_t R_{ss} + (1 - f_t) R_{sh} = 4f_t + 0 \cdot (1 - f_t) = 4f_t$$
- Hare: $$E_h(f_t) = f_t R_{hs} + (1 - f_t) R_{hh} = 3f_t + 2(1 - f_t)$$

Each individual's fitness is proportional to their payoff. Replicator dynamics determine the next generation:

$$\dot{f} = f_t \left( E_s(f_t) - \bar{E}(f_t) \right)$$

Where:
- $\bar{E}(f_t) = f_t E_s(f_t) + (1 - f_t) E_h(f_t)$ is the population's average fitness

Substituting in:
$$\bar{E}(f_t) = f_t(4f_t) + (1 - f_t)(3f_t + 2(1 - f_t))$$

The simulation discretizes this using stochastic sampling. At each generation, pairs of agents interact, accumulate payoffs, and the next generation is sampled via fitness-proportional selection.

## Folder Structure

```
project-root/
├── outputs/                         # Contains all CSVs and plots from simulation
│   ├── simulation_results.csv
│   ├── statistical_summary.csv
│   ├── fraction_stag_plot.png
│   ├── avg_payoff_plot.png
│   └── parameter_experiment_results.csv
└── scripts/                         # All source code for simulation and analysis
    ├── staghunt_simulation_lib.py
    ├── 01_staghunt_simulation.py
    ├── 02_statistical_analysis.py
    ├── 03_visualization.py
    └── 04_parameter_experiment.py
```

## Usage

### 1. Setup the Project:

Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Run the main simulation:
```bash
python scripts/01_staghunt_simulation.py
```
Generates: `outputs/simulation_results.csv`

### 3. Analyze the statistics:
```bash
python scripts/02_statistical_analysis.py
```
Generates: `outputs/statistical_summary.csv`

### 4. Visualize simulation results:
```bash
python scripts/03_visualization.py
```
Generates plots in `outputs/`

### 5. Run parameter sweep experiments:
```bash
python scripts/04_parameter_experiment.py
```
Generates: `outputs/parameter_experiment_results.csv`

## Requirements

Install all required Python packages with:
```bash
pip install -r requirements.txt
```

Required packages:
- numpy
- pandas
- matplotlib