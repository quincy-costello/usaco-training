"""
ID: quincy.3
TASK: ride
LANG: PYTHON3
"""

def get_number(string):
    nums = []
    num = 1
    for char in string:
        if char != "\n":
            nums.append(ord(char)-ord('A')+1)
    
    for i in nums:
        num *= i

    return num % 47

infile = open("ride.in", "r")
lines = infile.readlines()

outfile = open("ride.out", "w")
output = "GO\n" if get_number(lines[0]) == get_number(lines[1]) else "STAY\n"
outfile.write(output)