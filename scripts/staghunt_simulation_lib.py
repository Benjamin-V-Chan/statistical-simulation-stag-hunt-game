# Import necessary modules (random, numpy)
# Define function simulate_staghunt(params) where params is a dict:
#     - population_size: total number of players
#     - generations: number of simulation generations
#     - initial_stag_prob: initial probability to have "stag" as strategy
#     - payoff_matrix: dictionary with key (strategy1, strategy2) and value as tuple (payoff1, payoff2)
#     - baseline: small value to ensure nonzero selection probability
#     - seed: optional random seed for reproducibility
#
#   Initialize the population as a list of strategies ("stag" with probability initial_stag_prob, "hare" otherwise).
#   Create an empty list called results.
#   For each generation:
#       Shuffle the population randomly.
#       Create an array for individual payoffs (initialized to zero).
#       Pair individuals sequentially (if odd, leave the last unpaired, awarding it a small default payoff).
#       For each paired set:
#           Get the two strategies.
#           Look up their payoffs using the payoff_matrix.
#           Add the payoffs to the corresponding indices in the payoff array.
#       Calculate the average payoff for the generation.
#       Calculate the fraction of individuals using "stag".
#       Append a dict with generation number, fraction_stag, and average payoff to results.
#       Update the population using a replicator dynamic:
#           Compute selection probability for each individual as (individual payoff + baseline) divided by the total.
#           Sample a new population (with replacement) of the same size weighted by these probabilities.
#   Return the results list.
#
# (Optionally, additional helper functions can be defined here.)