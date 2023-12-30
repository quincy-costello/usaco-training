"""
ID: quincy.3
TASK: palsquare
LANG: PYTHON3
"""

def make_base(num, base): # num is in base 10
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_num = ""
    while num > 0:
        dig = num % base
        if dig < 10:
            new_num += str(dig)
        else:
            new_num += alph[dig - 10]

        num = num // base
        
    return new_num[::-1]

def is_pal(txt):
    if txt == txt[::-1]:
        return True
    
    return False

squares = []
for i in range(1, 301):
    squares.append([i, i**2])
    
infile = open("palsquare.in", "r")
base = int(infile.readline().strip())
infile.close()

palsquares = [] # list of pallindromic squares in base b (base in the infile)
for pair in squares:
    if is_pal(make_base(pair[1], base)):
        palsquares.append([make_base(pair[0], base), make_base(pair[1], base)])
        
outfile = open("palsquare.out", "w")
for pair in palsquares:
    print("%s %s" % (pair[0], pair[1]), file=outfile)

outfile.close()