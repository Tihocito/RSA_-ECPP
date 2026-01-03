from math import gcd

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % n
