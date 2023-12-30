"""
ID: quincy.3
TASK: transform
LANG: PYTHON3
"""

infile = open("transform.in", "r")
n = int(infile.readline())

start_rows = []
end_rows = []

def get_rows(rows):
    for i in range(n):
        tmp_row = []
        counter = 0
        for j in infile.readline().strip():
            counter += 1
            tmp_row.append(j)
            if counter == n:
                rows.append(tmp_row)

get_rows(start_rows)
get_rows(end_rows)

infile.close()

# 1: 90 Degree Rotation: Rotate Pattern 90 degrees clockwise
def rotate_90(start_rows):
    final_rows = [[0]*n for i in range(n)]
    for row in range(n):
        for col in range(n):
            final_rows[col][n - 1 - row] = start_rows[row][col]
    return final_rows

def reflect(start_rows):
    final_rows = [[0]*n for i in range(n)]
    for row in range(n):
        for col in range(n):
            final_rows[row][n - 1 - col] = start_rows[row][col]
    return final_rows

def main():
    if rotate_90(start_rows) == end_rows:
        return 1
    elif rotate_90(rotate_90(start_rows)) == end_rows:
        return 2
    elif rotate_90(rotate_90(rotate_90(start_rows))) == end_rows:
        return 3
    elif reflect(start_rows) == end_rows:
        return 4
    elif (
        rotate_90(reflect(start_rows)) == end_rows
        or rotate_90(rotate_90(reflect(start_rows))) == end_rows
        or rotate_90(rotate_90(rotate_90(reflect(start_rows)))) == end_rows
    ):
        return 5
    elif start_rows == end_rows:
        return 6
    else:
        return 7

outfile = open("transform.out", "w")
print("%s" % main(), file=outfile)