from ecpp_system.ecpp.ecpp_recursive import ecpp_prove

def test_small_prime():
    cert = ecpp_prove(13)
    assert cert is not None
