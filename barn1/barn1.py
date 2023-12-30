"""
ID: quincy.3
TASK: barn1
LANG: PYTHON3
"""

def count_boards(stalls):
    count = 0
    for i in range(len(stalls)):
        if stalls[i][1]:
            if i == 0:
                count += 1
            elif not stalls[i-1][1]:
                count += 1
    
    return count

def check_stalls(stalls):
    for stall in stalls:
        if not stall[0] and stall[1]:
            return False
        
    return True

infile = open("barn1.in", "r")

parse_ints = lambda line: [int(i) for i in line.split()]
max_boards, num_stalls, num_cows = parse_ints(infile.readline())
cows = [int(infile.readline()) for i in range(num_cows)]

infile.close()

stalls = []
for i in range(num_stalls):
    stall = [True, True] if (i+1) in cows else [False, True]
    stalls.append(stall)

for stall in stalls:
    if stall[1] and not stall[0]:
        stall[1] = False
    else:
        break

for i in range(len(stalls) - 1, -1, -1):
    if stalls[i][1] and not stalls[i][0]:
        stalls[i][1] = False
    else:
        break

while True:
    if count_boards(stalls) >= max_boards or check_stalls(stalls):
        break

    gap = []
    tmp_gap =[]
    for i in range(len(stalls)):
        if stalls[i][1] and not stalls[i][0]:
            tmp_gap.append(i)
        else:
            if len(tmp_gap) > len(gap):
                gap = tmp_gap
            tmp_gap = []

    for i in gap:
        stalls[i][1] = False

num_blocked = 0
for stall in stalls:
    if stall[1]:
        num_blocked += 1

outfile = open("barn1.out", "w")
print(num_blocked, file=outfile)