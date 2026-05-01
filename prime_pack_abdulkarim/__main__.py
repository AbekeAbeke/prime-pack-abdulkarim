import click
import random
from . import primes, checksum

@click.command()
@click.option('--count', default=1000)
@click.option('--seed', default=100)
def main(count, seed):
    nums = primes(count)
    random.seed(seed)
    random.shuffle(nums)
    print(checksum(nums))

if __name__ == "__main__":
    main()