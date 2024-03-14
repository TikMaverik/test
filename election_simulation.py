import random

num_times_a_wins = 0
num_times_b_wins = 0

trial_run = 10000
for i in range(0, trial_run):
    votes_for_a = 0
    votes_for_b = 0

    if random.random() < 0.42:
        votes_for_a += 1
    else:
        votes_for_b += 1

    if random.random() < 0.65:
        votes_for_a += 1
    else:
        votes_for_b += 1

    if random.random() < 0.17:
        votes_for_a += 1
    else:
        votes_for_b += 1

    if votes_for_a > votes_for_b:
        num_times_a_wins += 1
    else:
        num_times_b_wins += 1

print(f"Probability of A winning: {num_times_a_wins / trial_run}")
print(f"Probability of B winning: {num_times_b_wins / trial_run}")