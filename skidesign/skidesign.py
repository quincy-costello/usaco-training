"""
ID: quincy.3
TASK: skidesign
LANG: PYTHON3
"""

infile = open("skidesign.in", "r")
org_hills = [int(infile.readline()) for i in range(int(infile.readline()))]
infile.close()

hills = list(org_hills)

costs = []
for i in range(84):
    cost = 0
    hills = list(org_hills)
    for j in range(len(hills)):
        if hills[j] not in range(i, i + 17 + 1):
            if hills[j] > i + 17:
                hills[j] = i + 17
            else:
                hills[j] = i
        cost += (org_hills[j] - hills[j])**2
    costs.append(cost)

outfile = open("skidesign.out", "w")
print(min(costs), file=outfile)
outfile.close()