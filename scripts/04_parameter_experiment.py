import os
import pandas as pd
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
    
    for p in init_probs:
        for rep in range(replicates):
            params = base_params.copy()
            params["initial_stag_prob"] = p
            params["seed"] = 1000 + rep  # Different seed per replicate
            sim_result = simulate_staghunt(params)
            final_state = sim_result[-1]
            exp_results.append({
                "initial_stag_prob": p,
                "replicate": rep,
                "final_fraction_stag": final_state["fraction_stag"],
                "final_avg_payoff": final_state["avg_payoff"]
            })
    
    df_exp = pd.DataFrame(exp_results)
    output_dir = os.path.join("..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "parameter_experiment_results.csv")
    df_exp.to_csv(output_file, index=False)
    print("Parameter experiments complete. Summary:")
    print(df_exp.groupby("initial_stag_prob").agg({"final_fraction_stag": ["mean", "std"], "final_avg_payoff": ["mean", "std"]}))

if __name__ == "__main__":
    main()