import statistics

# create a list of infection rates
infection_rates = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# calculate and print statistics
print(f"Minimum: {min(infection_rates)}")
print(f"Maximum: {max(infection_rates)}")
print(f"Range: {max(infection_rates) - min(infection_rates)}")
print(f"Mean: {statistics.mean(infection_rates)}")
print(f"Median: {statistics.median(infection_rates)}")
print(f"Variance: {statistics.variance(infection_rates)}")
print(f"Standard deviation: {statistics.stdev(infection_rates)}")
