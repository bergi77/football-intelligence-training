import pandas as pd

csv_path = r"C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv"
df = pd.read_csv(csv_path)

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# Szűrés ligára és szezonra
league_season_df = df.loc[(df["league"] == "algir1") & (df["season"] == "2024-2025")]
print(league_season_df.shape)
print(league_season_df.head())

# Szűrés csapatra (hazai vagy vendég) a liga+szezon szűrésen belül
team = "ES Setif"
team_df = league_season_df.loc[
    (league_season_df["home_team"] == team) | (league_season_df["away_team"] == team)
]
print(team_df.shape)
print(team_df.head())

# iloc példa: az első 5 sor, kiválasztott oszlopok
print(team_df.iloc[:5, [0, 1, 3, 7, 8, 11, 12]])

# Rendezés a legtöbb gólos meccsek szerint, top 5
top5_goals = df.sort_values("total_goals", ascending=False).head(5)
print(top5_goals[["league", "season", "match_date", "home_team", "away_team", "home_goals", "away_goals", "total_goals"]])

# Új oszlop: gólkülönbség
df["goal_diff"] = df["home_goals"] - df["away_goals"]
print(df[["home_team", "away_team", "home_goals", "away_goals", "goal_diff"]].head())

# 1. Mekkora a hazai győzelmek aránya az összes meccshez képest?
home_win_rate = (df["result"] == "H").mean()
print(home_win_rate)

# 2. Melyik ligában a legmagasabb az átlagos gólszám meccsenként?
avg_goals_by_league = df.groupby("league")["total_goals"].mean().sort_values(ascending=False)
print(avg_goals_by_league.head())

# 3. Melyik csapat szerezte a legtöbb hazai gólt összesen?
top_home_scorers = df.groupby("home_team")["home_goals"].sum().sort_values(ascending=False)
print(top_home_scorers.head())

# 4. Hogyan alakul a döntetlenek aránya szezononként?
draw_rate_by_season = df.groupby("season")["result"].apply(lambda r: (r == "D").mean())
print(draw_rate_by_season.head())

# 5. Melyik csapat kapta a legtöbb gólt hazai pályán (leggyengébb hazai védelem)?
worst_home_defense = df.groupby("home_team")["away_goals"].sum().sort_values(ascending=False)
print(worst_home_defense.head())

# 6. Melyik ligában a legnagyobb a hazai pálya előnye (átlagos gólkülönbség)?
avg_goal_diff_by_league = df.groupby("league")["goal_diff"].mean().sort_values(ascending=False)
print(avg_goal_diff_by_league.head())

# 7. Átlagosan hány perc alatt esik az első gól ligánként?
avg_first_goal_time_by_league = df.groupby("league")["first_goal_time"].mean().sort_values()
print(avg_first_goal_time_by_league.head())

# 8. Hány meccset játszottak szezononként?
matches_per_season = df.groupby("season").size().sort_values(ascending=False)
print(matches_per_season.head())

# 9. Melyik csapatnak a legjobb a győzelmi aránya hazai és vendég meccseken összesítve?
home_wins = df.loc[df["result"] == "H", "home_team"].value_counts()
away_wins = df.loc[df["result"] == "A", "away_team"].value_counts()
total_wins = home_wins.add(away_wins, fill_value=0).sort_values(ascending=False)
print(total_wins.head())

# 10. Hány gól nélküli (0:0) meccs volt országonként?
goalless_by_country = df.loc[df["total_goals"] == 0].groupby("country").size().sort_values(ascending=False)
print(goalless_by_country.head())

