# Football Intelligence – Pandas Training (Level 1)

## Goal
Practice Pandas fundamentals on the `football_charts_matches.csv` match data: loading,
exploration, filtering, sorting, new columns, grouping, and simple statistics.

## Data
Path: `C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv`

Columns: `league`, `league_name`, `country`, `season`, `match_date`, `time`, `kickoff_utc`,
`home_team`, `away_team`, `ht_result`, `ft_result`, `home_goals`, `away_goals`, `total_goals`,
`result` (H/D/A), `first_goal_time`, `all_goal_times`.

## Practice exercises

Work in the `exercises.py` file, solving each exercise in its own function.

### Basics (review)
1. Load the CSV and print the `shape`, `dtypes`, and the number of missing values per column.
2. Filter for any league and season, then count the matches.
3. Sort the matches by `total_goals` descending, print the top 10.

### New columns
4. Create a boolean `is_draw` column (`result == "D"`).
5. Create a `high_scoring` column that is `True` when `total_goals >= 4`.
6. Convert `match_date` to `datetime`, and derive a `month` and a `weekday` column from it.

### Grouping (groupby)
7. Compute the average `total_goals` and match count per league in one go
   (`.agg(["mean", "count"])`).
8. Compute each team's home win rate
   (number of home wins / number of home matches).
9. Which months (from the `month` column in exercise 6) have the highest average goals?

### More advanced questions
10. Build a "form" indicator: the results (`W`/`D`/`L`) of a chosen team's last 5 matches
    in chronological order (hint: filter by team, sort by date, `.tail(5)`).
11. Pivot table: leagues (rows) vs. seasons (columns), value = average `total_goals`
    (`pd.pivot_table`).
12. Which team pairings (`home_team` + `away_team`) have played each other the most?
    (`value_counts` on a combined column).

## Tip
Print the intermediate result (`print`) for each exercise to verify your logic before
moving on to the next step.
