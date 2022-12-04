lines = [x for x in open("input.txt").readlines()]
p1_map = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}
p2_map = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}
print(f"Part 1: {sum(p1_map[line] for line in lines)}, Part 2: {sum(p2_map[line] for line in lines)}")
