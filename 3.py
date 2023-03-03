total = 0
smallest = None
largest = None
average = 0
infections = []

for i in range(1,8):
    num_infected = int(input("Enter the number of infection for the day {i}: "))
    infections.append(num_infected)
    total += num_infected

    if smallest is None or num_infected<smallest:
        smallest = num_infected

    if largest is None or num_infected>largest:
        largest = num_infected

average = total / len(infections)

print(f"Total number of infection: {total}")
print(f"Average number of infection: {average:.2f}")
print(f"Smallest number of infection: {smallest}")
print(f"Largest number of infection: {largest}")
