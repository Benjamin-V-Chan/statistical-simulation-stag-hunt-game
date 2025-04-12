import os
import pandas as pd
import numpy as np
from staghunt_simulation_lib import simulate_staghunt

def main():
    init_probs = [0.1, 0.3, 0.5, 0.7, 0.9]
    replicates = 5
    exp_results = []
    base_params = {
        "population_size": 200,
        "generations": 150,
        "payoff_matrix": {
            ("stag", "stag"): (4, 4),
            ("stag", "hare"): (0, 3),
            ("hare", "stag"): (3, 0),
            ("hare", "hare"): (2, 2)
        },
        "baseline": 1e-6
    }
    
