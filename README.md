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
