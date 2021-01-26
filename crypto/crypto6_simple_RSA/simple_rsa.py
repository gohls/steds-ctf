import random
import math


def generate_key(key_size):
    '''
        SIMPLE RSA ALGORITHM
    '''
    # Step 1. Compute N as the product of two prime numbers p and q:
    p = generate_big_prime(key_size)
    print('p prime =', p)
    q = generate_big_prime(key_size)
    print('q prime =', q)
    n = p * q
    print('n =', n)
    phi = (p - 1) * (q - 1)
    print('phi =', phi)
    # Step 2: Find e that are relatively prime to N:
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if math.gcd(e, phi) == 1:
            break
    print('e relatively prime to n = ', e)
    # Step 3: Find d, the modular inverse of e and for which e*d = 1 mod phi:
    d = modular_inv(e, phi)
    print('d modular inverse of e =', d)
    public_key = (e, n)
    private_key = (d, n)
    print('Public key pair:', public_key)
    print('Private key pair:', private_key)
    return public_key, private_key


def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = random.randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p


def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = random.randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True


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
    key, n = private_key
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(public_key, ciphertext):
    key, n = public_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def main():
    public_key, private_key = generate_key(8)
    message = 'Fly by the seats of your pants'
    encrypted_msg = encrypt(private_key, message)
    print('Encrypted message (separated by word): \n', encrypted_msg)
    print('Encrypted message joined (only for signle word encryption): ')
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print(decrypt(public_key, encrypted_msg))

if __name__ == '__main__':
    main()

