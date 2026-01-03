from .modarith import modinv

class ECPoint:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    def is_infinity(self):
        return self.x is None

    def __add__(self, other):
        n = self.curve.n

        if self.is_infinity():
            return other
        if other.is_infinity():
            return self
        if self.x == other.x and (self.y + other.y) % n == 0:
            return ECPoint(None, None, self.curve)

        if self.x == other.x:
            lam = (3*self.x*self.x + self.curve.a) * modinv(2*self.y, n) % n
        else:
            lam = (other.y - self.y) * modinv(other.x - self.x, n) % n

        x3 = (lam*lam - self.x - other.x) % n
        y3 = (lam*(self.x - x3) - self.y) % n
        return ECPoint(x3, y3, self.curve)

    def __rmul__(self, k):
        result = ECPoint(None, None, self.curve)
        addend = self
        while k > 0:
            if k & 1:
                result = result + addend
            addend = addend + addend
            k >>= 1
        return result
