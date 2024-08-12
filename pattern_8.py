# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

# *****
#  ***
#   *



def nStarTriangle(n: int) -> None:
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(2*(n-i)-1):
            print("*", end="")
        print()
    
nStarTriangle(3)