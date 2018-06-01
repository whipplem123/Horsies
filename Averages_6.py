import pickle

solutions = []
horses = []
matchups = []
for i in range(6):
    horses.append([i * 6 + 1, i * 6 + 2, i * 6 + 3, i * 6 + 4, i * 6 + 5, i * 6 + 6])
for a in range(8):
    for b in range(8):
        if b == a:
            continue
        for c in range(8):
            if c == b or c == a:
                continue
            for d in range(8):
                if d == a or d == b or d == c:
                    continue
                for e in range(8):
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in range(8):
                        if f in [a,b,c,d,e]:
                            continue
                        if a + b + c + d + e + f == 15:
                            solutions.append([a,b,c,d,e,f])

possibilities = [[0 for y in range(len(solutions[0]))] for x in range(len(solutions))]
for i in range(len(solutions)):
    for j in range(len(solutions[i])):
        possibilities[i][j] = horses[j][solutions[i][j]]

for i in range(len(possibilities)):
    print(possibilities[i])

schedule = [[[0 for horse in range(6)] for group in range(6)] for week in range(7)]
# Week 1
for i in range(36):
    schedule[0][i // 6][i % 6] = i + 1
# Week 2
for i in range(36):
    schedule[1][i % 6][i // 6] = i + 1

for i in range(7):
    print(schedule[i])

# Update matchups
for i in range(36):
    matchups.append([0 for y in range(36 - i)])
for i in range(len(matchups)):
    matchups[i][0] = 1
for i in range(len(matchups)):
    print(i + 1, matchups[i])

possible_weeks = []
i = 0
for a in range(120):
    print(a)
    pa = set(possibilities[a])
    for b1 in range(120):
        b = b1 + 120
        pb = set(possibilities[b])
        if not pb.isdisjoint(pa):
            continue
        for c1 in range(120):
            c = c1 + 240
            pc = set(possibilities[c])
            if not (pc.isdisjoint(pb) and pc.isdisjoint(pa)):
                continue
            for d1 in range(120):
                d = d1 + 360
                pd = set(possibilities[d])
                if not (pd.isdisjoint(pc) and pd.isdisjoint(pb) and pd.isdisjoint(pa)):
                    continue
                for e1 in range(120):
                    e = e1 + 480
                    pe = set(possibilities[e])
                    if not(pe.isdisjoint(pd) and pe.isdisjoint(pc) and pe.isdisjoint(pb) and pe.isdisjoint(pa)):
                        continue
                    for f1 in range(120):
                        f = f1 + 600
                        pf = set(possibilities[f])
                        if not(pf.isdisjoint(pe) and pf.isdisjoint(pd) and pf.isdisjoint(pc) and pf.isdisjoint(pb) and pf.isdisjoint(pa)):
                            continue
                        possible_weeks.append([possibilities[a], possibilities[b], possibilities[c], possibilities[d], possibilities[e], possibilities[f]])

print(len(possible_weeks))

f = open('store_possible_weeks', 'wb')
pickle.dump(possible_weeks, f)
f.close()

# To load:
# f = open('store_possible_weeks', 'rb')
# possible_weeks = pickle.load(f)
# f.close()
