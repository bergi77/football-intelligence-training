import pandas as pd

csv_path = r"C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(csv_path)


# 1. Basic exploration: shape, dtypes, missing values
def exercise_01(df: pd.DataFrame) -> None:
    pass


# 2. Filter by league and season, count matches
def exercise_02(df: pd.DataFrame) -> None:
    pass


# 3. Sort by total_goals, top 10
def exercise_03(df: pd.DataFrame) -> None:
    pass


# 4. is_draw column
def exercise_04(df: pd.DataFrame) -> None:
    pass


# 5. high_scoring column
def exercise_05(df: pd.DataFrame) -> None:
    pass


# 6. match_date -> datetime, month, weekday columns
def exercise_06(df: pd.DataFrame) -> None:
    pass


# 7. Average total_goals and match count per league
def exercise_07(df: pd.DataFrame) -> None:
    pass


# 8. Home win rate per team
def exercise_08(df: pd.DataFrame) -> None:
    pass


# 9. Average goals per month
def exercise_09(df: pd.DataFrame) -> None:
    pass


# 10. A team's form over its last 5 matches (W/D/L)
def exercise_10(df: pd.DataFrame, team: str) -> None:
    pass


# 11. Pivot table: league vs. season, average total_goals
def exercise_11(df: pd.DataFrame) -> None:
    pass


# 12. Most frequent team matchups
def exercise_12(df: pd.DataFrame) -> None:
    pass


if __name__ == "__main__":
    data = load_data()
    exercise_01(data)
