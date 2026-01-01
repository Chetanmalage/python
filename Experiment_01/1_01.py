# Write a Python program to exchange (swap) the values of two variables.


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping:")
print("a =", a, "b =", b)

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a, "b =", b)