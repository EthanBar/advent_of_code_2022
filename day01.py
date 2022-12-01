lines = [x for x in open("input.txt").readlines()]

calories = []
current = 0
for line in lines:
    if line == "":
        calories.append(current)
        current = 0
    else:
        current += int(line)
calories.sort()
print(f"Part 1: {calories[-1]}, Part 2: {sum(calories[-3:])}")
