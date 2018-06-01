import pickle
import time
import sys

# Load possible weeks
f = open('store_possible_weeks', 'rb')
possible_weeks = pickle.load(f)
f.close()

l = len(possible_weeks)

i = 0
for week in possible_weeks:
    if week[0][0] == 1 and week[0][1] == 8 and (15 not in week[0] or 22 not in week[0] or 29 not in week[0] and 36 not in week[0]):
        possible_weeks.remove(week)

print(len(possible_weeks))
f = open('store_possible_weeks', 'wb')
pickle.dump(possible_weeks, f)
f.close()