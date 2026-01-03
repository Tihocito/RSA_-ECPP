import hashlib

def hash_message(msg):
    return int.from_bytes(hashlib.sha256(msg).digest(), 'big')


def sign(msg, keypair):
    h = hash_message(msg)
    return pow(h, keypair.d, keypair.n)


def verify(msg, sig, keypair):
    h = hash_message(msg)
    return pow(sig, keypair.e, keypair.n) == h
