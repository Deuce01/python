def calculate_total_goals(team_goals, team_conceded, opponent_goals, opponent_conceded):
    # Calculate average goals scored and conceded by the team
    avg_team_goals = sum(team_goals) / len(team_goals)
    avg_team_conceded = sum(team_conceded) / len(team_conceded)
    
    # Calculate average goals scored and conceded by the opponents
    avg_opponent_goals = sum(opponent_goals) / len(opponent_goals)
    avg_opponent_conceded = sum(opponent_conceded) / len(opponent_conceded)
    
    # Calculate total goals to be scored in the next game
    total_goals = (avg_team_goals + avg_team_conceded + avg_opponent_goals + avg_opponent_conceded) / 2
    return total_goals

# Get goals from the user for the last five games
team_goals = []
team_conceded = []
opponent_goals = []
opponent_conceded = []

print("Enter goals scored and conceded by your team and opponents for the last five games:")

for i in range(5):
    team_goals.append(int(input("Enter goals scored by your team in game {}: ".format(i+1))))
    team_conceded.append(int(input("Enter goals conceded by your team in game {}: ".format(i+1))))
    opponent_goals.append(int(input("Enter goals scored by the opponents in game {}: ".format(i+1))))
    opponent_conceded.append(int(input("Enter goals conceded by the opponents in game {}: ".format(i+1))))

# Calculate total goals for the next game
total_goals = calculate_total_goals(team_goals, team_conceded, opponent_goals, opponent_conceded)
print("Total goals to be scored in the next game:", total_goals)
