import re
tests = int(input())
for i in range(0, tests):
    m = re.search('[A-Z][A-Z][A-Z][A-Z][A-Z]\d\d\d\d[A-Z]', input())
    if m is not None:
        print ('YES')
    else:
        print ('NO')