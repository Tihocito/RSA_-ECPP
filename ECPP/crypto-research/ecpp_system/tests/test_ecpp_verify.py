from ecpp_system.ecpp.ecpp_recursive import ecpp_prove
from ecpp_system.ecpp.verify import verify_certificate

def test_verify():
    cert = ecpp_prove(10007)
    assert verify_certificate(cert)
