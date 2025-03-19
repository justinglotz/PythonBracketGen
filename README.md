# PythonBracketGen

Created a little python script to try and help me fill out March Madness brackets this year. Each matchup is based on the number of times that a particular seed has won in that round of the tournament. For example, in the first round, a 1 seed has beaten a 16 seed 150 times, and the 16 has won 2 times. For this particular matchup, the program chooses a random number between 1 and 152. If that number is 150 or less, the 1 seed moves on. I tried to keep a "realistic chance of chaos" in that upsets still happen, as they will still be based on historical wins. The tiebreaker of total points scored is a random number between 140 and 155, with the hope to get somewhere close to the average for championship games. 

