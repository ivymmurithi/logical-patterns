import math

def worst_count(n: int):
    counter = 0
    
    for i in str(n):
        digit = int(i)
        counter += 1
    print(counter)
    
worst_count(329823)

def best_count(n: int):
    counter = int(math.log10(n) + 1)
    print(counter)

best_count(329823)


def countDigits(n: int) -> int:
    counter = 0

    while n > 0:
        counter += 1
        n //= 10
    
    return counter

countDigits(45638)