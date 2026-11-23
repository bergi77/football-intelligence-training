import pandas as pd

csv_path = r"C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(csv_path)


# 1. Alapfelfedezés: shape, dtypes, hiányzó értékek
def exercise_01(df: pd.DataFrame) -> None:
    pass


# 2. Szűrés ligára és szezonra, meccsek száma
def exercise_02(df: pd.DataFrame) -> None:
    pass


# 3. Rendezés total_goals szerint, top 10
def exercise_03(df: pd.DataFrame) -> None:
    pass


# 4. is_draw oszlop
def exercise_04(df: pd.DataFrame) -> None:
    pass


# 5. high_scoring oszlop
def exercise_05(df: pd.DataFrame) -> None:
    pass


# 6. match_date -> datetime, month, weekday oszlopok
def exercise_06(df: pd.DataFrame) -> None:
    pass


# 7. Ligánkénti átlagos total_goals és meccsek száma
def exercise_07(df: pd.DataFrame) -> None:
    pass


# 8. Csapatonkénti hazai győzelmi arány
def exercise_08(df: pd.DataFrame) -> None:
    pass


# 9. Hónaponkénti átlagos gólszám
def exercise_09(df: pd.DataFrame) -> None:
    pass


# 10. Egy csapat utolsó 5 meccsének formája (W/D/L)
def exercise_10(df: pd.DataFrame, team: str) -> None:
    pass


# 11. Pivot tábla: liga vs. szezon, átlagos total_goals
def exercise_11(df: pd.DataFrame) -> None:
    pass


# 12. Leggyakoribb csapatpárosok
def exercise_12(df: pd.DataFrame) -> None:
    pass


if __name__ == "__main__":
    data = load_data()
    exercise_01(data)
