# statistical-simulation-stag-hunt-game

## Project Overview

This project simulates the **Stag Hunt Game**, an evolutionary game-theoretic model of coordination. In this game, two individuals may choose to cooperate (hunt stag) or act selfishly (hunt hare). Cooperation yields higher rewards if both choose to cooperate, but defecting ensures a smaller, safer payoff. This simulation models population-level dynamics over many generations using replicator dynamics, a key mechanism in evolutionary game theory.

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