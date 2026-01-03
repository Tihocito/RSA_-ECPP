from rsa_system.keygen import RSAKeyPair
from rsa_system.signature import sign, verify

def test_signature():
    key = RSAKeyPair.generate(512)
    msg = b"RSA + ECPP"
    sig = sign(msg, key)
    assert verify(msg, sig, key)
