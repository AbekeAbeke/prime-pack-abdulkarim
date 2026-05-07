from prime_pack_abdulkarim import is_prime, primes, checksum, pipeline


def test_is_prime():
    assert is_prime(-7) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(29) is True
    assert is_prime(43) is True
    assert is_prime(97) is True
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(49) is False
    assert is_prime(100) is False
    assert is_prime(121) is False


def test_primes():
    result = primes(5)
    assert result == [2, 3, 5, 7, 11]
    assert primes(0) == []
    assert primes(2) == [2, 3]
    assert len(primes(10)) == 10
    assert primes(1) == [2]
    assert primes(10)[-1] == 29
    assert primes(12) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def test_checksum():
    assert checksum([]) == 0
    assert checksum([1]) == 113
    assert checksum([2, 3, 5]) == 2924666
    assert checksum([1, 2, 6, 24]) == 6012369


def test_pipeline():
    assert pipeline() == 7785816
