import random
import math


def generate_key(key_size):
    '''
        SIMPLE RSA ALGORITHM WITH INPUTS
    '''
    # Step 1. Compute N as the product of two prime numbers p and q:
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    print('p prime =', p)
    q = int(input("Enter another prime number (Not one you entered above): "))
    print('q prime =', q)
    n = p * q
    print('n =', n)
    phi = (p - 1) * (q - 1)
    print('phi =', phi)
    # Step 2: Find e that are relatively prime to N:
    e = int(input("Enter e relatively prime to n: "))
    print('e = ', e)
    # Step 3: Find d, the modular inverse of e and for which e*d = 1 mod phi:
    d = modular_inv(e, phi)
    print('d modular inverse of e =', d)
    public_key = (n, e)
    private_key = (n, d)
    print('Public key pair:', public_key)
    print('Private key pair:', private_key)
    return public_key, private_key


def modular_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def encrypt(private_key, plaintext):
    n, key = private_key
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(public_key, ciphertext):
    n, key = public_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def main():
    public_key, private_key = generate_key(8)
    print('Your encrypted message (separate numbers by space): ')
    encrypted_msg = [int(x) for x in input().split()]
    print(decrypt(public_key, encrypted_msg))


if __name__ == '__main__':
    main()

