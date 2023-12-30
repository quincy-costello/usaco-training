"""
TASK: crypt1
ID: quincy.3
LANG: PYTHON3
"""

infile = open("crypt1.in", "r")
dig_list = [int(dig) for dig in infile.readlines()[1].split()]
infile.close()

# Returns list of all possible numbers of length len that use the digits in dig_list <- (parameter)
def get_nums(dig_list, len):
    if len > 1:
        num_list = []
        for num in get_nums(dig_list, len-1):
            for dig in dig_list:
                num_list.append(int(str(dig) + str(num)))
        return num_list
    else:
        return list(dig_list)

def get_validity(prod, dig_list, num_len): # returns bool: False = invald, True = valid
    if len(str(prod)) == num_len:
        for c in str(prod):
            if int(c) in dig_list:
                continue
            return False
    else:
        return False
    return True
    
count = 0
for i in get_nums(dig_list, 3):
    for j in get_nums(dig_list, 2):
        if (get_validity(int(str(j)[1]) * i, dig_list, 3)
                and get_validity(int(str(j)[0]) * i, dig_list, 3)
                and get_validity(i * j, dig_list, 4)):
            count += 1

outfile = open("crypt1.out", "w")
print(count, file=outfile)
outfile.close()