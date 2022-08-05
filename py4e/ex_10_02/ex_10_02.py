name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From '): continue
    hours = words[5].split(':')
    counts[hours[0]] = counts.get(hours[0], 0) + 1
for key, val in sorted(counts.items()):
    print(key, val)
