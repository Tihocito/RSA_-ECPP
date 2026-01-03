def verify_certificate(cert):
    if cert is None:
        return False

    # Base prime
    if cert.subcert is None:
        return True

    n = cert.n
    m = cert.order
    q = cert.factor

    # Check structure n − 1 = q · k
    if m != n - 1:
        return False
    if m % q != 0:
        return False

    return verify_certificate(cert.subcert)
