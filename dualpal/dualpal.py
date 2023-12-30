"""
ID: quincy.3
TASK: dualpal
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

def is_palindromic(string):
    if string == string[::-1]:
        return True
    return False

infile = open("dualpal.in", "r")
line = infile.readline()
infile.close()

n = ""
s = ""
x = False
for char in line:
    if not x:
        n += char
    else:
        s += char
    
    if char == " ":
        x = True

n = int(n)
s = int(s)

nums = []
num = s
while len(nums) < n:
    flag = False
    num += 1
    pal = 0
    for base in range(2, 11):
        if is_palindromic(str(make_base(num, base))): # if the current number is a palindrome in this base
            for b in range(2, 11):
                if b != base:
                    if is_palindromic(str(make_base(num, b))):
                        nums.append(num)
                        flag = True
                        break
        if flag:
            break

outfile = open("dualpal.out", "w")
for num in nums:
    print(num, file=outfile)
outfile.close()