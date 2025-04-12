# Import necessary modules (os, pandas, numpy) and staghunt_simulation_lib.
# Define a list of different initial_stag_prob values (e.g., 0.1, 0.3, 0.5, 0.7, 0.9).
# Set up other simulation parameters (population_size, generations, payoff_matrix, baseline, seed).
# Initialize an empty list to collect experiment results.
# For each initial_stag_prob in the list:
#     For a fixed number of replications (e.g., 5 replicates):
#         Set simulation parameters with the current initial_stag_prob and a modified seed.
#         Run simulate_staghunt() to get results.
#         Take the final generation result (last element in returned list).
#         Append a dict with parameters (initial_stag_prob, replication id, final fraction_stag, final avg_payoff) to the list.
# Aggregate all the results into a pandas DataFrame.
# Write the aggregated results to a CSV file (e.g., outputs/parameter_experiment_results.csv).
# Print a brief summary of the experiments.