# To write a Python program that demonstrates the use of built-in string functions for string manipulation.

# Input string
s = " Hello Python Programming "

print("Original String:")
print(repr(s))
print("-" * 50)

# 1. Length of string
print("Length:", len(s))

# 2. Convert to lowercase
print("Lowercase:", s.lower())

# 3. Convert to uppercase
print("Uppercase:", s.upper())

# 4. Capitalize first letter
print("Capitalize:", s.capitalize())

# 5. Title case
print("Title:", s.title())

# 6. Swap case
print("Swapcase:", s.swapcase())

# 7. Strip spaces
print("Strip:", s.strip())
print("Left Strip:", s.lstrip())
print("Right Strip:", s.rstrip())

# 8. Replace substring
print("Replace:", s.replace("Python", "Java"))

# 9. Find substring
print("Find 'Python':", s.find("Python"))

# 10. Index substring
print("Index 'Programming':", s.index("Programming"))

# 11. Count substring
print("Count 'o':", s.count("o"))

# 12. Startswith
print("Startswith 'Hello':", s.strip().startswith("Hello"))

# 13. Endswith
print("Endswith 'Programming':", s.strip().endswith("Programming"))

# 14. Split string
words = s.split()
print("Split:", words)

# 15. Join strings
joined = "-".join(words)
print("Join:", joined)

# 16. Check alphanumeric
print("Is Alphanumeric:", s.strip().replace(" ", "").isalnum())

# 17. Check alphabetic
print("Is Alphabetic:", "Hello".isalpha())

# 18. Check digits
print("Is Digit:", "12345".isdigit())

# 19. Check numeric
print("Is Numeric:", "12345".isnumeric())

# 20. Check lowercase
print("Is Lowercase:", "hello".islower())

# 21. Check uppercase
print("Is Uppercase:", "HELLO".isupper())

# 22. Check title
print("Is Title:", "Hello World".istitle())

# 23. Check whitespace
print("Is Space:", " ".isspace())

# 24. Center alignment
print("Center:", s.strip().center(40, '*'))

# 25. Left justify
print("Ljust:", s.strip().ljust(40, '-'))

# 26. Right justify
print("Rjust:", s.strip().rjust(40, '-'))

# 27. Partition
print("Partition:", s.partition("Python"))

# 28. rpartition
print("RPartition:", s.rpartition("Programming"))

# 29. Zfill
print("Zfill:", "123".zfill(6))

# 30. Encode
encoded = s.encode()
print("Encoded:", encoded)

# 31. Casefold
print("Casefold:", s.casefold())

print("-" * 50)
print("All string functions executed successfully.")