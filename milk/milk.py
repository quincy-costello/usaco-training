"""
ID: quincy.3
TASK: milk
LANG: PYTHON3
"""

infile = open("milk.in", "r")

first_line = infile.readline().split()
req_gallons, num_farmers = int(first_line[0]), int(first_line[1])

farmers = []
for i in range(num_farmers):
    stats = []
    for j in infile.readline().split():
        stats.append(int(j))

    farmers.append(stats) # First one is price per gallon, second one is total number of gallons

infile.close()
farmers.sort()

current_gallons = 0
current_price = 0

for farmer in farmers:
    current_price += farmer[0] * farmer[1]
    current_gallons += farmer[1]

    if current_gallons >= req_gallons:
        current_price -= (current_gallons - req_gallons) * farmer[0]
        break

outfile = open("milk.out", "w")
print(current_price, file=outfile)
outfile.close()