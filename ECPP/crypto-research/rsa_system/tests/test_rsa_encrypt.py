from rsa_system.keygen import RSAKeyPair
from rsa_system.rsa_core import RSA

def test_encrypt_decrypt():
    key = RSAKeyPair.generate(512)
    rsa = RSA(key)
    msg = 123456
    c = rsa.encrypt(msg)
    m = rsa.decrypt(c)
    assert m == msg
