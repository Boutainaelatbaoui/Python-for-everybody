import re
hand = open('Sample-Data.txt')
numlist = list()
for line in hand:
    line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    result = sum([int(i) for i in stuff])
    numlist.append(result)
print(sum(numlist))
