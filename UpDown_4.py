import itertools

up_down = [[1,1,-1,-1],
           [1,-1,1,-1],
           [1,-1,-1,1]]

schedule = [[[0 for horse in range(4)] for group in range(4)] for week in range(5)]
schedule[0] = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]]

schedule[1] = [[1,5,9,13],
               [2,6,10,14],
               [3,7,11,15],
               [4,8,12,16]]

for i in range(5):
    for j in range(4):
        schedule[i][j][0] = j + 1

for j in range(3):
    schedule[j + 2][0][1] = j + 6

for i in range(len(schedule)):
    print(schedule[i])

l = 0
for indices in itertools.permutations(range(3), 3):
    for index in indices:
        l += 1