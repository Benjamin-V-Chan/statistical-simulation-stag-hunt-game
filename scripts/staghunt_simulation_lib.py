import random
import numpy as np

def simulate_staghunt(params):
    pop_size = params.get("population_size", 100)
    generations = params.get("generations", 100)
    init_prob = params.get("initial_stag_prob", 0.5)
    payoff_matrix = params.get("payoff_matrix", {
        ("stag", "stag"): (4, 4),
        ("stag", "hare"): (0, 3),
        ("hare", "stag"): (3, 0),
        ("hare", "hare"): (2, 2)
    })
    baseline = params.get("baseline", 1e-6)
    seed = params.get("seed", None)
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    population = ["stag" if random.random() < init_prob else "hare" for _ in range(pop_size)]
    results = []
