# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import math

master_frequency = {
    "E": 11.53,
    "T": 9.75,
    "A": 8.46,
    "O": 8.08,
    "H": 7.71,
    "N": 6.73,
    "R": 6.29,
    "I": 5.84,
    "S": 5.56,
    "D": 4.74,
    "L": 3.92,
    "W": 3.08,
    "U": 2.59,
    "G": 2.48,
    "F": 2.42,
    "B": 2.19,
    "M": 2.18,
    "Y": 2.02,
    "C": 1.58,
    "P": 1.08,
    "K": 0.84,
    "V": 0.59,
    "Q": 0.17,
    "J": 0.07,
    "X": 0.07,
    "Z": 0.03,
}

frequency = {
    "count": 0,
    "E": ["", 0],
    "T": ["", 0],
    "A": ["", 0],
    "O": ["", 0],
    "H": ["", 0],
    "N": ["", 0],
    "R": ["", 0],
    "I": ["", 0],
    "S": ["", 0],
    "D": ["", 0],
    "L": ["", 0],
    "W": ["", 0],
    "U": ["", 0],
    "G": ["", 0],
    "F": ["", 0],
    "B": ["", 0],
    "M": ["", 0],
    "Y": ["", 0],
    "C": ["", 0],
    "P": ["", 0],
    "K": ["", 0],
    "V": ["", 0],
    "Q": ["", 0],
    "J": ["", 0],
    "X": ["", 0],
    "Z": ["", 0],
}

# Your code here
# open the cipher and create file for decrypted txt
originalFile = open("applications/crack_caesar/ciphertext.txt", 'r')
decrypted = open("applications/crack_caesar/decrypted.txt", 'w')

# count each letter in the cipher
for ch in originalFile.read():
    if ch in frequency:
        frequency[ch][1] += 1
        frequency["count"] += 1
        
# calculate the freq of each letter and check if its close to master freq
for ch in frequency:
    if ch != 'count':
        frequency[ch][1] = round((frequency[ch][1] / frequency['count']) * 100, 2)
        
        for mch in master_frequency:
            if math.isclose(frequency[ch][1], master_frequency[mch]):
                frequency[ch][0] = mch
                
# reset the pointer of the cipher file to beginning
originalFile.seek(0)

# write decrypted file
for ch in originalFile.read():
    if ch in frequency:
        decrypted.write(frequency[ch][0])
    else:
        decrypted.write(ch)

originalFile.close()
decrypted.close()

# import text & make it a list
#  init a dict of count and a-z keys with vals of 0
    #  for cd in range(ord('A'), ord('Z') + 1):
    #      frequency[chr(cd)] = 0
# loop through txt
# if letter, increase its count in dict by 1  and val of 'count' by 1
#  loop again and swap freq value for corresponding letter
#  loop through and swap each letter

