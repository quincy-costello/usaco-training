"""
ID: quincy.3
TASK: friday
LANG: PYTHON3
"""
days = {"sat" : 0, "sun" : 0, "mon" : 0, "tues" : 0, "wed" : 0, "thurs" : 0, "fri" : 0}
days_keys = list(days.keys())

infile = open("friday.in", "r")
n = int(infile.readline().strip())
num_days = 0
num_days = ((n-(n//4))*365) + ((n//4)*366)

valid_dates_not_leap = [13, 44, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347]
valid_dates_leap = [13, 44, 73, 104, 134, 165, 195, 226, 257, 287, 318, 348]
num_days_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap = False
year_num = 1
day = days_keys[2]
for year in range(1900, 1900+n):
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 != 0 and year % 4 == 0:
        leap = True
    else:
        leap = False

    for month in range(1, 13):
        days[days_keys[(days_keys.index(day)+12) % 7]] += 1
        if month == 2 and leap:
            day = days_keys[(days_keys.index(day) + (num_days_for_month[month] + 1)) % 7]
        else:
            day = days_keys[(days_keys.index(day) + num_days_for_month[month]) % 7]

        # print(year, month, leap, days)

outfile = open("friday.out", "w")
for key in days_keys:
    if days_keys.index(key) == len(days_keys) - 1:
        outfile.write("%s" % days[key])
    else:
        outfile.write("%s " % days[key])
outfile.write("\n")

infile.close()
outfile.close()