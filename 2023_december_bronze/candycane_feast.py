import sys

infile = sys.stdin
infile.readline()

cows = infile.readline().split()
canes = infile.readline().split()
for i in range(len(cows)):
    cows[i] = int(cows[i])
for i in range(len(canes)):
    canes[i] = int(canes[i])

for i in range(len(canes)):
    distance = 0
    init_cane = canes[i]
    for j in range(len(cows)):
        
        org_cane = canes[i]
        if cows[j] > distance:
            canes[i] = init_cane - cows[j]
            canes[i] = 0 if canes[i] < 0 else canes[i]

            cows[j] += org_cane - canes[i]
            distance += org_cane - canes[i]

outfile = sys.stdout
for cow in cows:
    print(cow, file=outfile)