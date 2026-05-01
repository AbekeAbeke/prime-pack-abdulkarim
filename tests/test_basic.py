Version: 1
from prime_pack_abdulkarim import is_prime, primes, checksum, pipeline
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(1) == False

def test_primes():
    result = primes(5)
    assert result == [2, 3, 5, 7, 11]
    assert len(primes(10)) == 10

def test_checksum():
    assert checksum([]) == 0
    assert checksum([1]) == 113
    assert checksum([1, 2, 6, 24]) == 6012369

def test_pipeline():
    assert pipeline() == 7785816