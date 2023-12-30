"""
ID: quincy.3
LANG: PYTHON3
TASK: beads
"""

infile = open("beads.in", "r")
n = int(infile.readline().strip())
beads = infile.readline().strip()
tmp_list_beads = []
max_beads = 0
tmp_beads = 0
current_bead = ""

def count_beads(i, color, up):
    num_beads = 0
    while tmp_list_beads[i] not in [color, "x"]:
        num_beads += 1
        tmp_list_beads[i] = "x"
        if up:
            i += 1
        else:
            i -= 1
        i %= n

    return num_beads

def case(up, i):
    global tmp_beads
    if up:
        i += 1
        i %= n

    if beads[i] == "r":
        tmp_beads += count_beads(i, "b", up)
    elif beads[i] == "b":
        tmp_beads += count_beads(i, "r", up)
    else:
        while tmp_list_beads[i] == "w":
            tmp_beads += 1
            tmp_list_beads[i] = "x"
            if up:
                i += 1
            else:
                i -= 1
            i %= n
        
        if tmp_list_beads[i] == "r":
            tmp_beads += count_beads(i, "b", up)
        elif tmp_list_beads[i] == "b":
            tmp_beads += count_beads(i, "r", up)

    return tmp_beads

for i in range(n):
    tmp_list_beads = list(beads)
    case(False, i)
    case(True, i)
    if tmp_beads > max_beads:
        max_beads = tmp_beads
        tmp_beads = 0
    else:
        tmp_beads = 0

outfile = open("beads.out", "w")
outfile.write("%s\n" % max_beads)

infile.close()
outfile.close()