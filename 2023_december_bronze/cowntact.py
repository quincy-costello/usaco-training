import sys

def equal(num1, num2):
    if num1 % 2 == 1:
        num1 += 1
    if num2 % 2 == 1:
        num2 += 1

    return num1 == num2

infile = sys.stdin
infile.readline()

cows = infile.readline().strip()

groups = []
sublist = []
edge = False
for i in range(len(cows)):
    if (cows[i] == "1"):
        sublist.append(int(cows[i]))
        if i in (0, len(cows) - 1):
            edge = True
    elif len(sublist) > 0:
        sublist.append(edge)
        groups.append(sublist)
        sublist = []
        edge = False
if len(sublist) > 0:
    sublist.append(True)
    groups.append(sublist)

smallest = list(groups[0])
for group in groups:
    if equal(len(group) - 1, len(smallest) - 1):
        if not group[-1]:
            smallest = list(group)
    elif len(group) - 1 < len(smallest) - 1:
        smallest = list(group)

print(smallest)

if smallest[-1]: # if this group is on an edge
    days = len(smallest) - 1 - 1
else:            # else if this group is in the middle
    if (len(smallest) - 1) % 2 == 0:
        days = ((len(smallest) - 1) / 2) - 1
    else:
        days = (len(smallest) - 1) // 2

print(days)

infected = 0
for group in groups:
    if group[-1]: 
        infected += len(group) - (days) - 1
    else:
        infected += len(group) - (2 * days) - 1

outfile = sys.stdout
print(int(infected), file=outfile)