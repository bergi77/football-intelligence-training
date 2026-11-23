import pandas as pd

csv_path = r"C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv"
df = pd.read_csv(csv_path)

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# Filter by league and season
league_season_df = df.loc[(df["league"] == "algir1") & (df["season"] == "2024-2025")]
print(league_season_df.shape)
print(league_season_df.head())

# Filter by team (home or away) within the league+season filter
team = "ES Setif"
team_df = league_season_df.loc[
    (league_season_df["home_team"] == team) | (league_season_df["away_team"] == team)
]
print(team_df.shape)
print(team_df.head())

# iloc example: first 5 rows, selected columns
print(team_df.iloc[:5, [0, 1, 3, 7, 8, 11, 12]])

# Sort by highest-scoring matches, top 5
top5_goals = df.sort_values("total_goals", ascending=False).head(5)
print(top5_goals[["league", "season", "match_date", "home_team", "away_team", "home_goals", "away_goals", "total_goals"]])

# New column: goal difference
df["goal_diff"] = df["home_goals"] - df["away_goals"]
print(df[["home_team", "away_team", "home_goals", "away_goals", "goal_diff"]].head())

# 1. What share of matches are won by the home team?
home_win_rate = (df["result"] == "H").mean()
print(home_win_rate)

# 2. Which league has the highest average goals per match?
avg_goals_by_league = df.groupby("league")["total_goals"].mean().sort_values(ascending=False)
print(avg_goals_by_league.head())

# 3. Which team scored the most home goals overall?
top_home_scorers = df.groupby("home_team")["home_goals"].sum().sort_values(ascending=False)
print(top_home_scorers.head())

# 4. How does the draw rate change by season?
draw_rate_by_season = df.groupby("season")["result"].apply(lambda r: (r == "D").mean())
print(draw_rate_by_season.head())

# 5. Which team conceded the most goals at home (weakest home defense)?
worst_home_defense = df.groupby("home_team")["away_goals"].sum().sort_values(ascending=False)
print(worst_home_defense.head())

# 6. Which league has the biggest home-field advantage (average goal difference)?
avg_goal_diff_by_league = df.groupby("league")["goal_diff"].mean().sort_values(ascending=False)
print(avg_goal_diff_by_league.head())

# 7. On average, how many minutes until the first goal, by league?
avg_first_goal_time_by_league = df.groupby("league")["first_goal_time"].mean().sort_values()
print(avg_first_goal_time_by_league.head())

# 8. How many matches were played per season?
matches_per_season = df.groupby("season").size().sort_values(ascending=False)
print(matches_per_season.head())

# 9. Which team has the best combined win rate across home and away matches?
home_wins = df.loc[df["result"] == "H", "home_team"].value_counts()
away_wins = df.loc[df["result"] == "A", "away_team"].value_counts()
total_wins = home_wins.add(away_wins, fill_value=0).sort_values(ascending=False)
print(total_wins.head())

# 10. How many goalless (0:0) matches were there per country?
goalless_by_country = df.loc[df["total_goals"] == 0].groupby("country").size().sort_values(ascending=False)
print(goalless_by_country.head())


