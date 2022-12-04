lines = [x for x in open("input.txt").readlines()]

p1_score, p2_score = 0, 0
for line in lines:
    things = line.split(",")
    seg_1 = things[0].split("-")
    seg_2 = things[1].split("-")
    start_1, end_1 = int(seg_1[0]), int(seg_1[1])
    start_2, end_2 = int(seg_2[0]), int(seg_2[1])

    if (start_1 <= start_2 and end_2 <= end_1) or (start_2 <= start_1 and end_1 <= end_2):
        p1_score += 1
    if max(start_1, start_2) <= min(end_1, end_2):
        p2_score += 1
print(f"Part 1: {p1_score}, Part 2: {p2_score}")
