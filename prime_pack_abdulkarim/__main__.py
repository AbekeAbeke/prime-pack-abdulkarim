import click
import random
from . import primes, checksum

@click.command()
@click.option('--count', default=1000, help='Number of primes')
@click.option('--seed', default=100, help='Random seed')
def main(count: int, seed: int):
    nums = primes(count)
    random.seed(seed)
    random.shuffle(nums)
    print(checksum(nums))

if __name__ == "__main__":
    main()