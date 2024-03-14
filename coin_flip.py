import random



def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

heads_tally = 0
tails_tally = 0
for trial in range(1_000_000):
    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of fair heads to tails is {ratio}")


def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

heads_tally = 0
tails_tally= 0
for trial in range(1_000_000):
    if unfair_coin_flip(0.7) == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of unfair heads to tails is {ratio}")