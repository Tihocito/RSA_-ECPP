class ECPPCertificate:
    def __init__(self, n, curve, P, order, factor, subcert=None):
        self.n = n
        self.curve = curve
        self.P = P
        self.order = order
        self.factor = factor
        self.subcert = subcert
