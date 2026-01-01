# Convert temperature using conditionals:
#  Celsius → Fahrenheit
#  Fahrenheit → Celsius

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice: "))
temp = float(input("Enter temperature: "))
if choice == 1:
 result = (temp * 9/5) + 32
 print("Temperature in Fahrenheit:", result)
elif choice == 2:
 result = (temp - 32) * 5/9
 print("Temperature in Celsius:", result)
else:
 print("Invalid choice")