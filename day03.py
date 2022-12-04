lines = [x for x in open("input.txt").readlines()]

def priority(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1

p1_score = 0
for line in lines:
    A = set(line[:len(line) // 2])
    B = set(line[len(line) // 2:])
    p1_score += priority(list(A.intersection(B))[0])

p2_score = 0
for i in range(0, len(lines), 3):
    A = set(lines[i])
    B = set(lines[i + 1])
    C = set(lines[i + 2])
    p2_score += priority(list(A.intersection(B, C))[0])
print(f"Part 1: {p1_score}, Part 2: {p2_score}")
