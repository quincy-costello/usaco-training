"""
ID: quincy.3
TASK: gift1
LANG: PYTHON3
"""
infile = open("gift1.in", "r")
np = int(infile.readline())
group = {}
group_keys = []

for i in range(np):
    line = infile.readline().strip()
    group[line] = 0
    group_keys.append(line)

for i in range(np):
    name = infile.readline().strip()
    n = False
    num_dollars = ""
    num_people = ""
    for char in infile.readline().strip():
        if char == " ":
            n = True
            continue

        if not n:
            num_dollars += char
        else:
            num_people += char

    num_dollars = int(num_dollars)
    num_people = int(num_people)
    group[name] -= num_dollars
    if num_people != 0:
        group[name] += num_dollars % num_people
    
    for j in range(num_people):
        name = infile.readline().strip()
        group[name] += num_dollars // num_people

outfile = open("gift1.out", "w")
for i in range(np):
    outfile.write("%s %s\n" % (group_keys[i], group[group_keys[i]]))