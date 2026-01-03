from ecpp_system.ecpp.ecpp_recursive import ecpp_prove

def test_recursive():
    cert = ecpp_prove(10007)
    assert cert is not None
