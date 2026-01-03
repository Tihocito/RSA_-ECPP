import random
from ecpp_system.ecpp.ecpp_recursive import ecpp_prove

def miller_rabin(n, rounds=10):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits):
    while True:
        p = random.getrandbits(bits) | 1 | (1 << (bits - 1))
        if not miller_rabin(p):
            continue

        # ECPP verification (offline proof)
        cert = ecpp_prove(p)
        if cert is not None:
            return p, cert
