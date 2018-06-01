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
* For the nxn problem (with n prime), Week j is constructed by skipping j - 2 spots, 2 &le; j &le; n + 1

### Composite Numbers
The solution described above works for all prime numbers, but not for composite numbers.  For example, let's see what happens if we try this solution for the 4x4 problem.

|   | Race 1 | Race 2 | Race 3 | Race 4 |
| - | ------ | ------ | ------ | ------ |
| Week 1 | 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16 |
| Week 2 | 1 5 9 13 | 2 6 10 14 | 3 7 11 15 | 4 8 12 16 |
| Week 3 | 1 6 11 16 | 2 7 12 13 | 3 8 9 14 | 4 5 10 15 |
| Week 4 | 1 7 9 15 | 2 8 10 16 | 3 5 11 13 | 4 6 12 14 |
| Week 5 | 1 8 11 14 | 2 5 12 15 | 3 6 9 16 | 4 7 10 13 |

As you can see, we have instances of horses racing against each other twice and not racing against other horses at all.  We can see that in Week 4, when we skip 2 spots, we get duplicates from the third pod - when we skip 2 spots twice, we've skipped 4 spots, which wraps us back to a spot we've already seen (since 4 is divisible by 2).  Thus, we need to find a different solution for composite numbers.

### 4x4 Solution
Fortunately, for the relatively small 4x4 problem we can simply brute-force our way to a solution.  The solution is as follows:

|   | Race 1 | Race 2 | Race 3 | Race 4 |
| - | ------ | ------ | ------ | ------ |
| Week 1 | 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16 |
| Week 2 | 1 5 9 13 | 2 6 10 14 | 3 7 11 15 | 4 8 12 16 |
| Week 3 | 1 6 11 16 | 2 5 12 15 | 3 8 9 14 | 4 7 10 13 |
| Week 4 | 1 7 12 14 | 2 8 11 13 | 3 5 10 16 | 4 6 9 15 |
| Week 5 | 1 8 10 15 | 2 7 9 16 | 3 6 12 13 | 4 5 11 14 |

Note that the first two weeks are the same as for the prime numbers.  After that, the solutions differ.

### Observations
Now that we have an example of a solution for a composite number, we can compare the prime and composite solutions to find patterns that hold for both.  
* Average horse number in races from Week 3 on: For the 4x4 solution, this average is 34.  Note that 8.5 is also the average of all the horses 1-16.  In the 3x3 solution, the average for each race is 5, which is also the average of all the horses 1-9.
* Switching horses: We can actually arrive at the 4x4 solution by a series of switches.  Note that the problem occurs in Week 4 - thus we start by switching the last two horses between Races 1 and 4, as well as Races 2 and 3.  We then switch Race 2 in Weeks 3 and 5, as well as Race 4 in Weeks 3 and 5.  Finally, in Week 5 we switch the last two horses in Races 1 and 4, as well as Races 2 and 3.

### Challenges
The problem gets exponentially harder as we increase n.  For example, I have calculated that there are over 1 million possible weeks in the 6x6 problem.  Choosing the right 5 weeks out those 1 million is virtually impossible without some further insight.  This problem only gets worse for the 8x8 case.  Thus 4x4 is the largest composite number for which any kind of brute-force solution is feasible.  Another problem is that the number of divisors continues to increase with n.  As we know, our solution breaks down when n is composite.  For n = 4, problems occurred when we tried to skip 2 because 4 is divisible by 2.  For n = 8, problems will occur at skipping 2 and 4, meaning perhaps the adjustments we made to fix the 4x4 solution may be many times more complex.

### Description of Files
* Averages: this program uses the insight of the average horse number to construct a list of possible races, and then possible weeks, for a given problem.  This list can then be used to iterate through possible weeks and find a combination that solves the problem. 
* Schedule: this program builds on Averages by trying to construct a schedule from the list of possible weeks. Unfortunately, this doesn't appear to be practical even for the 6x6 problem. 
* UpDown: this program is based on observations from the 4x4 solution.  If we know Race 1 for each week, we can possibly generate the remaining races by moving two of the pod positions up and 2 down as we move left to right.  More work will need to be done to see if this can be applied to the 6x6 problem, or even if the assumption that we know Race 1 for every week can be fulfilled.
* store_possible_weeks: this is a file that stores the binary for the result of Averages_6, so that we don't have to run it every time we want to run Schedule (Averages_6 had a runtime of about 10 minutes).
