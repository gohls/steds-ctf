Given is a hex string that has been encrypted. A single byte XOR key will decrypt the string and reveal the plaintext=flag. This can be done by hand, and may be the faster way, instead of trying to write the code. It took me a day to write the code, although I did later find some code by googling the exact problem. So I may not be verbose in what needs to be done. 

But in theory: Turn the hex cipher into bytes, then run every possible XOR bitwise operation against the the cipher bytes. The one with most matches in the alpabet, is the flag. I made sure that "e" is the most use character, although, its not necessary.

See python program for solution and futher clarification
