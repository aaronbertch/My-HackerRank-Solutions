numStrings = int(input())
text = ''
length = 0
count = 0
for x in range(0, numStrings):
    text = input()
    length = len(text)
    for y in range(1, length):
        if(length == 1):
            break
        elif(text[y] != text[y-1]):
            continue
        else:
            count+=1
    print(count)
    count = 0
            