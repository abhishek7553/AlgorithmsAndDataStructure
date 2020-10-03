rom math import sqrt

def isPrime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True
