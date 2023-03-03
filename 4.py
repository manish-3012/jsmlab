import statistics

temperatures = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5]

mean = statistics.mean(temperatures)
median = statistics.median(temperatures)
mode = statistics.mode(temperatures)

print(f"Mean: {mean:.1f}")
print(f"Median: {median:.1f}")
print(f"Mode: {mode:.1f}")