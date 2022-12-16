from number_theory_functions import *

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """

        # Generate two large primes
        p = generate_prime(digits)
        q = generate_prime(digits)


        public_key, private_key = RSA.generate_keys_from_input(p,q)
        return RSA(public_key, private_key)

    @staticmethod
    def generate_keys_from_input(p, q):
        # Calculate N
        N = p * q 

        # Calculate phi(N)
        phi_N = (p-1)*(q-1) # = K

        # Choose e such that 1 < e < phi(N) and gcd(e, phi(N)) = 1
        e= find_e_in_U(phi_N)
        

        # Calculate d such that (d * e) % phi(N) = 1
        d = modular_inverse(e, phi_N)

        # Create the public and private keys
        public_key = (N, e)
        private_key = (N,d)

        return public_key, private_key
        
    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        N, e = self.public_key

        #Returns x to the power of y modulo p
        c = modular_exponent(m, e, N)
        return c


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N, d = self.private_key

        #Returns x to the power of y modulo p
        m = modular_exponent(c, d, N)
        return m

       