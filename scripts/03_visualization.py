import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    input_file = os.path.join("..", "outputs", "simulation_results.csv")
    df = pd.read_csv(input_file)
    
    output_dir = os.path.join("..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure()
    plt.plot(df["generation"], df["fraction_stag"])
    plt.xlabel("Generation")
    plt.ylabel("Fraction Stag")
    plt.title("Evolution of Stag Strategy")
    fraction_plot_file = os.path.join(output_dir, "fraction_stag_plot.png")
    plt.savefig(fraction_plot_file)
    plt.close()
    
    plt.figure()
    plt.plot(df["generation"], df["avg_payoff"])
    plt.xlabel("Generation")
    plt.ylabel("Average Payoff")
    plt.title("Average Payoff over Generations")
    payoff_plot_file = os.path.join(output_dir, "avg_payoff_plot.png")
    plt.savefig(payoff_plot_file)
    plt.close()
    
    print(f"Plots saved to {output_dir}")

if __name__ == "__main__":
    main()