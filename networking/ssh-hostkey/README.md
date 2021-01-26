Challenge:
ssh-hostkey

Solution:
To solve this challenge, use nmap to do an extended scan of the target. This will display the hostkey in hexidecimal format.

command: nmap -A ctf.stedwards.edu

Note: there are other ways of solving this problem, and it is possible to get the hostkey in ascii format. The flag was in hex though. I gave credit if you got ascii format.
