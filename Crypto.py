# Function to compute the greatest common divisor (GCD) using Euclid's algorithm
def gcd(a, b):
    """Calculate the greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def modular_inverse(e, phi):
    """Compute the modular inverse of e mod phi using the Extended Euclidean Algorithm."""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y
    
    g, x, _ = extended_gcd(e, phi)
    if g == 1:
        return x % phi
    else:
        raise ValueError("Modular inverse does not exist")

# Function to encrypt the message
def encrypt(message, e, n):
    """Encrypt the message using the public key (e, n)."""
    return [(ord(char) ** e) % n for char in message]

# Function to decrypt the message
def decrypt(encrypted_message, d, n):
    """Decrypt the message using the private key (d, n)."""
    return ''.join([chr((char ** d) % n) for char in encrypted_message])

# Given prime numbers
p = 23
q = 13

# Compute modulus n
n = p * q

# Compute Euler's Totient
phi = (p - 1) * (q - 1)

# Choose an encryption exponent e that is coprime with phi
e = 5

# Ensure e and phi are coprime
while gcd(e, phi) != 1:
    e += 2

# Compute the decryption exponent d
d = modular_inverse(e, phi)

# Display the expected output format
print("Expected Output:")
print(f"  Modulus n: {n}")
print(f"  Totient φ(n): {phi}")
print(f"  Public key (e, n): ({e}, {n})")
print(f"  Private key (d, n): ({d}, {n})")

# Words to encrypt and decrypt
words = ["Florida", "Orange", "Green", "Hill", "CIS", "FAMU", "Valid"]

for word in words:
    print(f"\nOriginal Message: {word}")
    
    # Encrypt the message
    encrypted_message = encrypt(word, e, n)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, d, n)
    print(f"Decrypted Message: {decrypted_message}")
