from ecpp_system.ecpp.ecpp_recursive import ecpp_prove
from ecpp_system.ecpp.verify import verify_certificate

if __name__ == "__main__":
    n = 10007
    cert = ecpp_prove(n)
    print("Number:", n)
    print("ECPP recursive proved:", verify_certificate(cert))
