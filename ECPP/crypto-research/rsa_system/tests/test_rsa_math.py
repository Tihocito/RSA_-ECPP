from rsa_system.math import modinv

def test_modinv():
    assert modinv(3, 11) == 4
