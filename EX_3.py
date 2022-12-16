from number_theory_functions import *
from rsa_functions import RSA

## EX 3 
"""
    The goal was to find the code, with e=3499, N=12215009, message=42.
    Therefore, we found that the division into prime factors of:12215009 is 12215009=3491 * 3499.
    With these factors, we found rsa_bob with "generate_keys_from_input" function.
    Then, we used "decrypt" function and returned the result.
    """
if __name__ == '__main__':
    e=3499
    y=42
    N = 12215009

    #The division into prime factors of:12215009 is 12215009=3491 * 349
    # phi_N = (3491-1)*(3499-1)
    rsa_bob = RSA(*RSA.generate_keys_from_input(3491,3499))
    x = rsa_bob.decrypt(y)
    print(x)