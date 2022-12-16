from rsa_functions import *
from number_theory_functions import *

"""
    The goal was to choose a message and a public key, 
    and to encode the message. our input is p=7919, q=6841.
    We found a public key and private key with RSA "generate_keys_from_input" function,
    and used "encrypt" function to encode the message.
    """
## EX 5 
if __name__ == '__main__':
   p=7919
   q=6841

   public_key, private_key = RSA.generate_keys_from_input(p,q)
   rsa_bob = RSA(public_key, private_key)

   rsa_Alice = RSA(public_key)
   
   messege = 314159

   y = rsa_Alice.encrypt(messege)