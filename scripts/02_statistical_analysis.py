import os
import pandas as pd

def main():
    input_file = os.path.join("..", "outputs", "simulation_results.csv")
    df = pd.read_csv(input_file)
    summary = df[["fraction_stag", "avg_payoff"]].describe()
    output_file = os.path.join("..", "outputs", "statistical_summary.csv")
    summary.to_csv(output_file)
    print("Statistical summary:")
    print(summary)

if __name__ == "__main__":
    main()