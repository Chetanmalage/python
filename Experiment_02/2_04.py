# Calculate displacement at different time intervals using the formula: 𝒙 = 𝑨𝒔𝒊𝒏(𝝎𝒕)

import math

A = float(input("Enter Amplitude: "))
w = float(input("Enter Angular Frequency: "))

t = 0
print("Time\tDisplacement")

while t <= 10:
 x = A * math.sin(w * t)
 print(t, "\t", round(x, 3))
 t += 1
