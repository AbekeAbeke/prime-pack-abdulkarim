# version 1
import random
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> list[int]:
    result = []
    n = 2

    while len(result) < count:
        if is_prime(n):
            result.append(n)
        n += 1
    return result

def checksum(x: list[int]) -> int:
    result = 0
    for value in x:
        result = (result + value) * 113
        result %= 10_000_007
    return result

def pipeline() -> int:
    nums = primes(1000)
    random.seed(100)
    random.shuffle(nums)
    return checksum(nums)   # ✅ MUST return