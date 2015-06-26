import string
import sys

len = int(input())
plainText = raw_input();
offset = int(input());
letter = 0;
alphabet = string.ascii_lowercase;
    
for x in range(0,len):
    if(plainText[x].islower() and plainText[x].isalpha()):
            letter = ord(plainText[x])- ord('a'); 
            sys.stdout.write(alphabet[(letter + offset) % 26]); 
    elif(plainText[x].isupper() and plainText[x].isalpha()):
            letter = ord(plainText[x])- ord('A'); 
            sys.stdout.write(alphabet[(letter + offset) % 26].upper()); 
    else:
            sys.stdout.write(plainText[x]);
            