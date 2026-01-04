# Implementing programs using written modules and Python Standard / Scientific
# Libraries (NumPy, Pandas, Matplotlib, SciPy).

# To implement a Python program using simple written logic (functions) and scientific
# libraries to analyze experimental data.

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy import stats 

# ---------- Written Functions ----------
def calculate_average(values):
    return sum(values) / len(values)

def experiment_status(avg):
    if avg >= 50:
        return "Successful"
    else:
        return "Failed"

# ---------- Input Section ----------
n = int(input("Enter number of readings: "))
readings = []

for i in range(n):
    value = float(input(f"Enter reading {i+1}: "))
    readings.append(value)

# ---------- Pandas DataFrame ----------
df = pd.DataFrame({
    "Reading_No": range(1, n + 1),
    "Value": readings
})

print("\nExperimental Data:")
print(df)

# ---------- NumPy Computation ----------
values_np = np.array(readings)
mean = np.mean(values_np)
std_dev = np.std(values_np)

print("\nMean =", mean)
print("Standard Deviation =", std_dev)

# ---------- Using Written Functions ----------
avg = calculate_average(readings)
status = experiment_status(avg)

print("Average =", avg)
print("Experiment Status =", status)

# ---------- SciPy Statistical Analysis ----------
z_scores = stats.zscore(values_np)
print("Z-Scores =", z_scores)

# ---------- Matplotlib Visualization ----------
plt.plot(df["Reading_No"], df["Value"], marker='o')
plt.xlabel("Reading Number")
plt.ylabel("Value")
plt.title("Experimental Readings Analysis")
plt.grid(True)
plt.show()
