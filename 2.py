hours = [0,5,10,15]

print(f"Hours\tBacteria")

for h in hours:
    bacteria = 200 * 2 ** (h)
    print(f"{h}\t{bacteria}")