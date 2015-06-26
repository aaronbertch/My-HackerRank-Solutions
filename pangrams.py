import string
import sys

text = input().lower()
alphabet = string.ascii_lowercase

for x in range(0, 25):
    if (alphabet[x] in text):
        continue
    else:
        print('not pangram')
        sys.exit()

print ('pangram')