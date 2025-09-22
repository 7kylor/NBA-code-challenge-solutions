import pandas as pd

# Load the data
df = pd.read_csv('Data/NBA2000-2009.csv')

# Part One: Find players with double-digit stats in at least 2 categories
# Calculate total rebounds
df['REB'] = df['OREB'] + df['DREB']

# Define the 5 main categories
categories = ['PTS', 'REB', 'AST', 'STL', 'BLK']

# Filter players who have >=10 in at least 2 categories
double_digit_mask = (df[categories] >= 10).sum(axis=1) >= 2

# Create the result DataFrame
double_double = df[double_digit_mask][['PLAYER', 'YEAR', 'PTS', 'AST', 'REB', 'STL', 'BLK']].copy()
double_double = double_double.rename(columns={'REB': 'REB', 'STL': 'STL', 'BLK': 'BLK'})

# Sort by year (ascending) then by player name (ascending)
double_double = double_double.sort_values(['YEAR', 'PLAYER'])

# Reset index
double_double = double_double.reset_index(drop=True)

# Part Two: Calculate most valuable players
# Calculate missed field goals and free throws
df['Missed_FG'] = df['FGA'] - df['FGM']
df['Missed_FT'] = df['FTA'] - df['FTM']

# Calculate player value for each season
df['VALUE'] = (df['PTS'] + df['OREB'] + df['DREB'] + df['AST'] + df['STL'] + df['BLK']) - (df['TOV'] + df['Missed_FG'] + df['Missed_FT'])

# Group by player and calculate average value over all seasons
player_avg_value = df.groupby('PLAYER')['VALUE'].mean().reset_index()

# Sort by value (descending) then by player name (ascending)
best_player = player_avg_value.sort_values(['VALUE', 'PLAYER'], ascending=[False, True])

# Round to 2 decimal places
best_player['VALUE'] = best_player['VALUE'].round(2)

# Reset index
best_player = best_player.reset_index(drop=True)

# Part Three: Find team with highest average points per year
# Group by year and team, sum the points
team_year_pts = df.groupby(['YEAR', 'TEAM'])['PTS'].sum().reset_index()

# Find the team with max points for each year
max_PTS_of_year = team_year_pts.loc[team_year_pts.groupby('YEAR')['PTS'].idxmax()]

# Round to 2 decimal places
max_PTS_of_year['PTS'] = max_PTS_of_year['PTS'].round(2)

# Sort by year (ascending)
max_PTS_of_year = max_PTS_of_year.sort_values('YEAR')

# Reset index
max_PTS_of_year = max_PTS_of_year.reset_index(drop=True)

# Display results
print("Part One - Double Double Players:")
print(double_double.head())
print("\nPart Two - Most Valuable Players:")
print(best_player.head())
print("\nPart Three - Team with Highest Average Points per Year:")
print(max_PTS_of_year.head())

