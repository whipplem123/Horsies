This repository contains various ideas I've had for how to solve the horse problem.

### Overview of the Problem
You have 64 horses and want to construct a schedule such that each horse is in a race against each other horse exactly once.  The horses will race 8 at a time, such that there will be 8 races per week for 9 weeks.  Since such a schedule consists of 8 races per week with 8 horses per week, I will refer to it as the 8x8 problem.  Similar schedules can be constructed for simpler problems, such as 4x4 or 5x5.

### Prime Numbers
When the number of horses per race is a prime number, the solution is trivial - there is a simple algorithm to generate the schedule.  For example, let's look at the 3x3 problem.

|   | Race 1 | Race 2 | Race 3 |
| - | ------- | ------- | ------- |
| Week 1 | 1 2 3 | 4 5 6 | 7 8 9 |
| Week 2 | 1 4 7 | 2 5 8 | 3 6 9 |
| Week 3 | 1 5 9 | 2 6 7 | 3 4 8 |
| Week 4 | 1 6 8 | 2 4 9 | 3 5 7 |

We start by grouping the horses into pods, and the first week consists of each of these pods racing against each other.  In the second week, we have races with the first in each pod against each other, the second against each other, and so on.  This pattern holds for the 4x4 problem as well, and I believe we can use this pattern for the first two weeks of any problem.  In the following weeks, Horse 1 will race in the first race, Horse 2 in the second, and so on.  Their opponents will be determined by picking one horse each from the remaining pods.  This decision is based on the horse's position within the pod.  The schedule is constructed as follows:
* Week 3: skip 1 - Horse 1 is the first horse in Pod 1, so he will race against the second horse from Pod 2 and the third horse from Pod 3.  When necessary, we will wrap back to the start of the pod.  Thus, Horse 2 will race against the third horse from Pod 2 and the first horse from Pod 3.
* Week 4: skip 2 - Horse 1 races against the third horse from Pod 2 and the second horse from Pod 3.  Similarly, Horse 2 races against the first horse from Pod 2 and the third horse from Pod 3.
For the nxn problem (with n prime), Week j is constructed by skipping j - 2 spots, up to j = n + 1.

### The 4x4 Problem
