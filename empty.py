from sortedcontainers import SortedSet

# Digits
origin = list(str(input("Enter the numbers : ")))

# count
total = len(origin)

# Unique
sett = SortedSet(origin)

# Unique Length
slen = len(set(sett))

# Relative Difference
diff = total - slen

# Zero Creator
zeros = []

# Driver Code
for x in range(diff):
    zeros.append(0)
print(*list(sett),*zeros, sep=" ")

#! Bug in arrangement order
