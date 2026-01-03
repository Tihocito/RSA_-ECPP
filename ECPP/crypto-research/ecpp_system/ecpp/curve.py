class EllipticCurve:
    def __init__(self, a, b, n):
        self.a = a % n
        self.b = b % n
        self.n = n

    def is_valid(self):
        return (4 * self.a**3 + 27 * self.b**2) % self.n != 0
