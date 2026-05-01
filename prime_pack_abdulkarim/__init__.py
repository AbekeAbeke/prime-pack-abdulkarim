import random

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(count: int) -> list[int]:
    result = []
    num = 2

    while len(result) < count:
        if is_prime(num):
            result.append(num)
        num += 1

    return result


def checksum(x: list[int]) -> int:
    result = 0
    for value in x:
        result = (result + value) * 113
        result %= 10_000_007
    return result