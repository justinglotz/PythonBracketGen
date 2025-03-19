import random

# Team lists with seeds
EastTeams = ['1. Duke', '2. Alabama', '3. Wisconsin', '4. Arizona', '5. Oregon', '6. BYU', '7. Saint Marys', '8. Mississippi St', '9. Baylor', '10. Vanderbilt', '11. VCU', '12. Liberty', '13. Akron', '14. Montana', '15. Robert Morris', '16. AMER/MSM']
SouthTeams = ['1. Auburn', '2. Michigan St', '3. Iowa St', '4. Texas A&M', '5. Michigan', '6. Ole Miss', '7. Marquette  ', '8. Louisville', '9. Creighton', '10. New Mexico', '11. North Carolina', '12. UC San Diego', '13. Yale', '14. Lipscomb', '15. Bryant', '16. Alabama St']
WestTeams = ['1. Florida', '2. St Johns', '3. Texas Tech', '4. Maryland', '5. Memphis', '6. Missouri', '7. Kansas', '8. UConn', '9. Oklahoma', '10. Arkansas', '11. Drake', '12. Colorado St', '13. Grand Canyon', '14. UNC Wilmington', '15. Omaha', '16. Norfolk St']
MidWestTeams = ['1. Houston', '2. Tennessee', '3. Kentucky', '4. Purdue', '5. Clemson', '6. Illinois', '7. UCLA', '8. Gonzaga', '9. Georgia', '10. Utah State', '11. TEX/XAV', '12. McNeese', '13. High Point', '14. Troy', '15. Wofford', '16. SIUE']

# Win statistics
roundOneWins = [150, 141, 130, 120, 99, 94, 93, 74, 78, 59, 58, 53, 32, 22, 11, 2]
roundTwoWins = [128, 95, 80, 72, 52, 44, 29, 16, 8, 24, 26, 22, 6, 2, 4, 0]
Sweet16Wins = [101, 68, 39, 23, 12, 16, 10, 9, 5, 9, 9, 2, 0, 0, 1, 0]
Elite8Wins = [60, 32, 17, 14, 9, 3, 3, 6, 2, 1, 5, 0, 0, 0, 0, 0]
Final4Wins = [37, 13, 11, 4, 4, 2, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0]
ChampWins = [24, 5, 4, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

# Winner function with team names and seeds
def winner(team1, team2, wins):
    team1Seed, team1Name = team1.split('. ')
    team2Seed, team2Name = team2.split('. ')
    team1Seed = int(team1Seed)
    total = wins[team1Seed - 1] + wins[int(team2Seed) - 1]
    odds = random.randint(1, total)
    
    if odds > wins[team1Seed - 1]:
        print(f'{team2Name} ({team2Seed}) advances!\n')
        return team2
    else:
        print(f'{team1Name} ({team1Seed}) advances!\n')
        return team1

# Print the results for each region

def display_results(region, teams, round1Wins, round2Wins, sweet16Wins, elite8Wins, final4Wins, champWins):
    print(f'{region} Region:')
    print('Round One Results:')
    a = winner(teams[0], teams[15], round1Wins)
    b = winner(teams[7], teams[8], round1Wins)
    c = winner(teams[4], teams[11], round1Wins)
    d = winner(teams[3], teams[12], round1Wins)
    e = winner(teams[5], teams[10], round1Wins)
    f = winner(teams[2], teams[13], round1Wins)
    g = winner(teams[6], teams[9], round1Wins)
    h = winner(teams[1], teams[14], round1Wins)

    print('Round Two Results:')
    i = winner(a, b, round2Wins)
    j = winner(c, d, round2Wins)
    k = winner(e, f, round2Wins)
    l = winner(g, h, round2Wins)

    print('Sweet 16 Results:')
    m = winner(i, j, sweet16Wins)
    n = winner(k, l, sweet16Wins)

    print(f'{region} Winner:')
    o = winner(m, n, elite8Wins)
    print('\n')
    return o

# Display results for each region
south_winner = display_results('SOUTH', SouthTeams, roundOneWins, roundTwoWins, Sweet16Wins, Elite8Wins, Final4Wins, ChampWins)
east_winner = display_results('EAST', EastTeams, roundOneWins, roundTwoWins, Sweet16Wins, Elite8Wins, Final4Wins, ChampWins)
west_winner = display_results('WEST', WestTeams, roundOneWins, roundTwoWins, Sweet16Wins, Elite8Wins, Final4Wins, ChampWins)
midwest_winner = display_results('MIDWEST', MidWestTeams, roundOneWins, roundTwoWins, Sweet16Wins, Elite8Wins, Final4Wins, ChampWins)

# Final Four
print('FINAL FOUR LEFT:')
final4L = winner(south_winner, west_winner, Final4Wins)

print('FINAL FOUR RIGHT:')
final4R = winner(east_winner, midwest_winner, Final4Wins)

# Champion
print('CHAMPION:')
champion = winner(final4L, final4R, ChampWins)

# Display random points scored by the champion
points_scored = random.randint(140, 155)
print(f'{champion} is the champion with {points_scored} points scored!')
