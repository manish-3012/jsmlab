import random

counts = [0]*6

for i in range(6000000):
    value = random.randrange(1,7)
    counts[value-1] +=1

print(f"Counts for the numbers are as follows: {counts}")