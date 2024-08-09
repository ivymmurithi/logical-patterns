# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N-dimensional forest.
# Example:

# Input: ‘N’ = 3

# Output: 
# * * *
# * * *
# * * *


def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

nForest(3)