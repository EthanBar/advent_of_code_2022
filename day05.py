lines = [x for x in open("input.txt").readlines()]
instructions = []
for line in lines[10:]:
    split_ = line.split(" ")
    instructions.append((int(split_[1]), int(split_[3]) - 1, int(split_[5]) - 1))

crates = [list("HBVWNMLP"), list("MQH"), list("NDBGFQML"), list("ZTFQMWG"),
    list("MTHP"), list("CBMJDHGT"), list("MNBFVR"), list("PLHMRGS"), list("PDBCN")]

def operate_crane(crates, is_9000):
    for amount, from_, to_ in instructions:
        if is_9000:
            crates[to_] += reversed(crates[from_][-amount:])
        else:
            crates[to_] += crates[from_][-amount:]
        crates[from_] = crates[from_][:-amount]
    return "".join([pile.pop() for pile in crates])

print(f"Part 1: {operate_crane(crates.copy(), True)}, "
      f"Part 2: {operate_crane(crates.copy(), False)}")

