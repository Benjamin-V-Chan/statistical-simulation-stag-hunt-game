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
    for gen in range(generations):
        random.shuffle(population)
        payoffs = np.zeros(pop_size)
        # Pair individuals sequentially
        num_pairs = pop_size // 2
        for i in range(num_pairs):
            idx1, idx2 = 2*i, 2*i+1
            strat1, strat2 = population[idx1], population[idx2]
            payoff1, payoff2 = payoff_matrix[(strat1, strat2)]
            payoffs[idx1] += payoff1
            payoffs[idx2] += payoff2
        # Handle odd individual if pop_size is odd
        if pop_size % 2 == 1:
            payoffs[-1] += np.mean(list(payoff_matrix.values()), axis=0)[0]  # assign a small average payoff
        avg_payoff = float(np.mean(payoffs))
        fraction_stag = population.count("stag") / pop_size
        results.append({"generation": gen, "fraction_stag": fraction_stag, "avg_payoff": avg_payoff})
        selection_probs = (payoffs + baseline) / np.sum(payoffs + baseline)
        indices = np.random.choice(pop_size, size=pop_size, p=selection_probs)
        population = [population[i] for i in indices]
    return results