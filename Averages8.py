solutions = []

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
                        for g in range(8):
                            if g in [a,b,c,d,e,f]:
                                continue
                            for h in range(8):
                                if h in [a,b,c,d,e,f,g]:
                                    continue
                                if a + b + c + d + e + f + g + h == 28:
                                    solutions.append([a,b,c,d,e,f,g,h])

for i in range(len(solutions)):
    print(solutions[i])
