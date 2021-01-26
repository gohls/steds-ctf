# plaintext: goat cheese on pizza like bee to honey
# XOR byte key: 01011000
# value: 88
from typing import List, Union

# 1 - variable for hex cipher
# 2 - byte array of cipher
# 3 - run all combination of xor key. rv [score, plaintext, xor key]
# 4 - print result
def main():
    xor_hex_cipher = '3F37392C783B303D3D2B3D783736782831222239783431333D783A3D3D782C37783037363D21'
    byte_array_cipher = hex_to_byte_array(xor_hex_cipher)
    score_plaintext_xor_key = find_single_byte_xor_key(byte_array_cipher)
    print(score_plaintext_xor_key)


def hex_to_byte_array(xor_hex_cipher):
    return bytearray.fromhex(xor_hex_cipher)


# Try every possible combination of XOR key of a single byte (256 values)
# XOR every character in cipher
# Run those XOR characters through a score function that counts alphabet matches
# Return the list with highest matches.
def find_single_byte_xor_key(byte_array_cipher):
    all_possible_combinations = []
    for i in range(256):
        characters = [chr(c ^ i) for c in byte_array_cipher]
        all_possible_combinations.append([score_of_alphabet_matches(characters), ''.join(characters), i])
    highest_score: List[Union[float, str, int]] = max(all_possible_combinations, key=lambda x: x[0])
    return highest_score


# Argument passed in is all characters from the cipher, against an XOR value
# Filter for only the matches of a-z, A-Z, and blanks.
# Return the float value. Float of 1.0 means, all characters matched.
def score_of_alphabet_matches(character_str):
    scr = filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'Z' or x == ' ', character_str)
    return float(len([x for x in scr])) / len(character_str)


if __name__ == "__main__":
    main()

