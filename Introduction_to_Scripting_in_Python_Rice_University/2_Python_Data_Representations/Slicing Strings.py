"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print(word[1:5])
print(word[5:9])
print()
# Open ended slices
print(word[5:])
print(word[:4])
print()
# Using negative indices
print(word[-3:])
print(word[2:-3])
print()
# Indexing past the end
print(word[8:20])
print("$" + word[22:29] + "^")
print()
# Empty slices
print(word[6:6])
print(word[4:2])
