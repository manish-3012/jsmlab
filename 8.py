dice_sum = range(2,13)

dice_prob = [0] * 11

for i in range(2,13):
    if i<=7:
        dice_prob[i-2] = (i-1)/36
    else:
        dice_prob[i-2] = (13-i)/36

expected_value = 0
for i in range(11):
    expected_value += dice_sum[i]*dice_prob[i]

print("Sum\tProbability")
for i in range(11):
    print(f"{dice_sum[i]}\t{dice_prob[i]:.3f}")
print(f"\nExpected value: {expected_value:.2f}")
