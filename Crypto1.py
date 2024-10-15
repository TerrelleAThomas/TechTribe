# Import necessary modules
from math import gcd

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def modular_inverse(e, phi):
    # Extended Euclidean Algorithm to find d such that (d * e) % phi == 1
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    g, x, _ = egcd(e, phi)
    if g == 1:
        return x % phi

# Function to encrypt the message
def encrypt(message, e, n):
    # Convert each character of the message to its integer representation and encrypt it
    encrypted_message = [(ord(char) ** e) % n for char in message]
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, d, n):
    # Decrypt each integer representation of the encrypted message and convert back to characters
    decrypted_message = ''.join([chr((char ** d) % n) for char in encrypted_message])
    return decrypted_message

# Given prime numbers
p = 23
q = 13

# Compute modulus n
n = p * q

# Compute Euler's Totient
phi = (p - 1) * (q - 1)

# Choose an encryption exponent e that is coprime with phi and 1 < e < phi
e = 5  # Common choices are 3, 5, or 65537, ensure e is coprime with phi

# Check that e and phi are coprime
while gcd(e, phi) != 1:
    e += 2

# Compute the decryption exponent d
d = modular_inverse(e, phi)

# Display the public and private keys
print(f"Public Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")

# Example message to encrypt and decrypt
message = "FAMU"

# Encrypt the message
encrypted_message = encrypt(message, e, n)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt(encrypted_message, d, n)
print(f"Decrypted Message: {decrypted_message}")