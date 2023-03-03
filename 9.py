import sys
import random
import seaborn as sns
import matplotlib.pyplot as plt

# Get number of rolls from command-line argument
var= int(input("Enter the no. of dice rolls:"))
num_rolls = var

# Generate random dice rolls
rolls = [random.randint(1, 6) for i in range(num_rolls)]

# Get frequency of each roll
freqs = [rolls.count(i) for i in range(1, 7)]

# Create bar plot using Seaborn
sns.set(style="whitegrid")
ax = sns.barplot(x=freqs, y=list(range(1, 7)), orient="h")

# Set plot title and labels
ax.set_title(f"{num_rolls} Dice Rolls")
ax.set_xlabel("Frequency")
ax.set_ylabel("Roll Value")

print(f'{freqs}')
# Show plot
plt.show()