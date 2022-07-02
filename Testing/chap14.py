# problem 1
# * * * * * * * * * *

print("Problem 1:")
for i in range(10):
    print("*", end=" ")
print('\n----------------')

# problem 2
# * * * * * * * * * *
# * * * * *
# * * * * * * * * * * * * * * * * * * * *

print("Problem 2:")
for i in range(10):
    print("*", end=" ")
print()
for j in range(5):
    print("*", end=" ")
print()
for k in range(20):
    print("*", end=' ')
print('\n----------------')


# problem 3
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *

print("Problem 3:")
for i in range(8):
    for j in range(10):
        print("*", end=" ")
    print()
print('\n----------------')

# problem 4
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("Problem 4:")
for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()
print('\n----------------')

# problem 5
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *

print("Problem 5:")
for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print()
print('\n----------------')

# problem 6
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    for j in range(10):
        print(j, end=' ')
    print()
print('\n----------------')

# problem 7 is similar to previous

for i in range(10):
    for j in range(10):
        print(i, end=' ')
    print()
print('\n----------------')

# problem 8
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    for j in range(i+1):
        print(j, end=' ')
    print()
print('\n----------------')

# problem 9 (alternate solution)
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

for i in range(10, -1, -1):
    for j in range(i):
        print(j, end=' ')
    print()

# Problem 9 (Orig)
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0

for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for j in range(10-i):
        print(j, end=" ")
    print()

# problem 10
# 1  2  3  4  5  6  7  8  9
# 2  4  6  8 10 12 14 16 18
# 3  6  9 12 15 18 21 24 27
# 4  8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81

# Hint:
"""
>>> print(f'{a}')
1
>>> print(f'{b}')
11

vs.

>>> print(f'{a:2d}')
 1
>>> print(f'{b:2d}')
11

"""

print()
for i in range(1, 10):
    for j in range(1, 10):
        if j < 10:
            print(f"{j} ", end=' ')
        elif j >= 10:
            print(f"{j}", end=' ')
