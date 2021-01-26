# Global variables
hexStr = '130E021B000D1A021244080A00080F4516184908185946001A03520D151C'
# taco tues every day all day
hexKeyStr = '7461636F20747565736461792065766572792064617920616C6C206461790A'


def main():
    binary = hex_to_binary(hexStr)
    binary_key = hex_to_binary(hexKeyStr)
    print('Hex value to XOR: ' + hexStr)
    print('HexStr binary: ' + binary)
    print('HexKeyStr KEY: ' + binary_key)
    xor = binary_to_xor(binary, binary_key)
    b = bytes(xor)
    print(b)


def hex_to_binary(hex_str):
    return bytes.fromhex(hex_str)


def binary_to_xor(binary_str, binary_key):
    return [a ^ b for (a, b) in zip(binary_str, cycle(binary_key))]


if __name__ == '__main__':
    main()
