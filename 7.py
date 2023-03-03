import matplotlib.pyplot as plt

infection_rates = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

days = list(range(1, len(infection_rates) + 1))

plt.bar(days, infection_rates)

plt.xlabel("Days")
plt.ylabel("Infection rates")
plt.title("COVID-19 Infection Rates for First 20 Days")

plt.show()