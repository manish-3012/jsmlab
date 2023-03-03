total_seconds = int(input("Enter number of seconds: "))

# calculate hours
hours = total_seconds // 3600
total_seconds %= 3600

# calculate minutes
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{hours} - {minutes} - {seconds}")