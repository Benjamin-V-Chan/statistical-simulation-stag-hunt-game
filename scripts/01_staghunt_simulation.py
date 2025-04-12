import os
import csv
from staghunt_simulation_lib import simulate_staghunt

def main():
    params = {
        "population_size": 200,
        "generations": 150,
        "initial_stag_prob": 0.6,
        "payoff_matrix": {
            ("stag", "stag"): (4, 4),
            ("stag", "hare"): (0, 3),
            ("hare", "stag"): (3, 0),
            ("hare", "hare"): (2, 2)
        },
        "baseline": 1e-6,
        "seed": 42
    }
    results = simulate_staghunt(params)
    output_dir = os.path.join("..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "simulation_results.csv")
    with open(output_file, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["generation", "fraction_stag", "avg_payoff"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Simulation complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()