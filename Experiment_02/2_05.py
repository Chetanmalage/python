# Calculate average of experimental readings and determine experiment validity

n = int(input("Enter number of readings: "))
total = 0

for i in range(n):
 value = float(input(f"Enter reading {i+1}: "))
 total += value

avg = total / n
print("Average =", avg)

if avg >= 50:
 print("Experiment Successful")
else:
 print("Experiment Failed")