import random



def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

heads_tally = 0
tails_tally = 0
total_flips = 0
num_repeat = 10_000_000
for trial in range(num_repeat):

    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1 


    if (heads_tally >= 1) and (tails_tally >= 1):
        total_flips += 1
        heads_tally = 0
        tails_tally = 0

    

ratio = num_repeat / total_flips
print(f"The ratio of fair heads to tails is {ratio:.2f}")