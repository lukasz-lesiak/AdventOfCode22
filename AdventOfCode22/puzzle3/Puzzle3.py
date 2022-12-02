f = open("../inputs/day2_input.txt", "r")
# f = open("../inputs/day2_test_input.txt", "r")
strategyGuide = f.read().split('\n')
figureScore = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
outcomeScore = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
score = 0
for encounter in strategyGuide:
    score += figureScore[encounter[2]]
    score += outcomeScore[encounter[0]][encounter[2]]

print(score)
