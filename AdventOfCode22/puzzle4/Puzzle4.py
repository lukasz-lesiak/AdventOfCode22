f = open("../inputs/day2_input.txt", "r")
# f = open("../inputs/day2_test_input.txt", "r")
strategyGuide = f.read().split('\n')
outcomeScore = {
    "A": {"X": 0+3, "Y": 3+1, "Z": 6+2},
    "B": {"X": 0+1, "Y": 3+2, "Z": 6+3},
    "C": {"X": 0+2, "Y": 3+3, "Z": 6+1},
}
score = 0
for encounter in strategyGuide:
    score += outcomeScore[encounter[0]][encounter[2]]

print(score)
