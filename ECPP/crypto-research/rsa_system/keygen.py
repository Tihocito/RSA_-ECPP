from .prime_provider import generate_prime
from .math import modinv

class RSAKeyPair:
    def __init__(self, n, e, d, p, q, p_cert, q_cert):
        self.n = n
        self.e = e
        self.d = d
        self.p = p
        self.q = q
        self.p_cert = p_cert
        self.q_cert = q_cert

    @staticmethod
    def generate(bits=2048):
        e = 65537
        p, p_cert = generate_prime(bits // 2)
        q, q_cert = generate_prime(bits // 2)

        n = p * q
        phi = (p - 1) * (q - 1)
        d = modinv(e, phi)

        return RSAKeyPair(n, e, d, p, q, p_cert, q_cert)
