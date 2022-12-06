line = [x for x in open("input.txt").readlines()][0]
def first_n_unique(n, i=0):
    for i in range(len(line)):
        if len(set(line[i:i+n])) == n:
            return i + n
print(f"Part 1: {first_n_unique(4)}, Part 2: {first_n_unique(14)}")
