from binascii import hexlify, unhexlify


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y


def modular_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def str2int(s):
    return int(hexlify(bytes(s.encode())), 16)


def int2str(n):
    h = hex(n)
    return unhexlify(h[2: len(h)])


class RSAKey(object):
    def __init__(self, mod, exp):
        self.mod = mod
        self.exp = exp


def encrypt(public, plaintext):
    return pow(str2int(plaintext), public.exp, public.mod)


def decrypt(private, ciphertext):
    return int2str(pow(ciphertext, private.exp, private.mod))


def main():
    n = 0x01A3900C7CD5B305
    d = 0x025F2D1619EF1ABD  # public
    c = 0x28f4f650c37ff9  # str(goatRSA) <= 7 bytes
    p = 113511859
    q = 1040388199
    # e = 54799875512748133
    phi = (p - 1) * (q - 1)
    e = modular_inv(d, phi)
    public_key = RSAKey(n, d)
    private_key = RSAKey(n, e)

    assert decrypt(private_key, encrypt(public_key, 'test')) == b'test'

    print(decrypt(private_key, c))

    ''' Uncomment to encrypt a message '''
    # encrypt_msg = encrypt(public_key, 'goatRSA')  # str <= 7 bytes
    # print('enc = ', hex(encrypt_msg))


if __name__ == '__main__':
    main()
