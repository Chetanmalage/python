# Write a Python program to circulate the values of n variables to the left.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

print("Before circulation:")
print("a =", a, "b =", b, "c =", c)

# Left circulation
a, b, c = b, c, a

print("After circulation:")
print("a =", a, "b =", b, "c =", c)