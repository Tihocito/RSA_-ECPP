class RSA:
    def __init__(self, keypair):
        self.key = keypair

    def encrypt(self, m):
        return pow(m, self.key.e, self.key.n)

    def decrypt(self, c):
        return pow(c, self.key.d, self.key.n)
