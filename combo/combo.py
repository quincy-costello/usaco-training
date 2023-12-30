"""
ID: quincy.3
TASK: combo
LANG: PYTHON3
"""
from itertools import product

infile = open("combo.in", "r")
dial = [i + 1 for i in range(int(infile.readline()))]
f_combo = [int(c) for c in infile.readline().split()]
m_combo = [int(c) for c in infile.readline().split()]
infile.close()

f_ranges = [[dial[i%len(dial)] for i in range(num-3, num+2)] for num in f_combo]
m_ranges = [[dial[i%len(dial)] for i in range(num-3, num+2)] for num in m_combo]

combos = set()
for p in product(f_ranges[0], f_ranges[1], f_ranges[2]):
    combos.add(p)
for p in product(m_ranges[0], m_ranges[1], m_ranges[2]):
    combos.add(p)

outfile = open("combo.out", "w")
print(len(combos), file=outfile)
outfile.close()