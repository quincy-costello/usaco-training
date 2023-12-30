"""
ID: quincy.3
TASK: milk2
LANG: PYTHON3
"""

infile = open("milk2.in", "r")
n = int(infile.readline())

start_times = []
end_times = []
for i in infile.readlines():
    start_end = i.split()
    start_times.append(int(start_end[0]))
    end_times.append(int(start_end[1]))

start_times.sort()
end_times.sort()

num_farmers = 0
start_index = 0
end_index = 0
milking_time = 0
max_milking_time = 0
no_milking_time = 0
max_no_milking_time = 0

for time in range(end_times[n-1] + 1):
    if num_farmers > 0:
        milking_time += 1
        if no_milking_time > max_no_milking_time:
            max_no_milking_time = no_milking_time
        no_milking_time = 0
    if num_farmers <= 0 and time > start_times[0]:
        no_milking_time += 1
        if milking_time > max_milking_time:
            max_milking_time = milking_time
        milking_time = 0

    while start_index < n and time == start_times[start_index]:
        num_farmers += 1
        start_index += 1
    while end_index < n and time == end_times[end_index]:
        num_farmers -= 1
        end_index += 1
        
if milking_time > max_milking_time:
    max_milking_time = milking_time
if no_milking_time > max_no_milking_time:
    max_no_milking_time = no_milking_time

outfile = open("milk2.out", "w")
print("%s %s" % (max_milking_time, max_no_milking_time), file=outfile)

infile.close()
outfile.close()