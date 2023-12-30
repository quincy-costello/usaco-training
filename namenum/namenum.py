"""
ID: quincy.3
TASK: namenum
LANG: PYTHON3
"""

keypad_map = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PRS",
    8 : "TUV",
    9 : "WXY"
}

infile = open("namenum.in", "r")
serial = int(infile.readline().strip())
infile.close()

valids = open("dict.txt", "r")

final_names = []
new_serial = ""
for name in valids:
    for letter in name.strip():
        for num in keypad_map:
            if letter in keypad_map[num]:
                new_serial += str(num)
                break
    if int(new_serial) == serial:
        final_names.append(name.strip())
    new_serial = ""

valids.close()
final_names.sort()

outfile = open("namenum.out", "w")
for name in final_names or ["NONE"]:
    print(name, file=outfile)
outfile.close()