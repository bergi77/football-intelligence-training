# Football Intelligence – Pandas gyakorló anyag (1. szint)

## Cél
A `football_charts_matches.csv` mérkőzés-adatokon gyakorolni a Pandas alapjait: betöltés,
felfedezés, szűrés, rendezés, új oszlopok, csoportosítás, és egyszerű statisztikák.

## Adat
Útvonal: `C:\szemelyes_papir2\FI\1_hét\football_charts_matches_v2026.10\football_charts_matches.csv`

Oszlopok: `league`, `league_name`, `country`, `season`, `match_date`, `time`, `kickoff_utc`,
`home_team`, `away_team`, `ht_result`, `ft_result`, `home_goals`, `away_goals`, `total_goals`,
`result` (H/D/A), `first_goal_time`, `all_goal_times`.

## Gyakorló feladatok

Dolgozz az `exercises.py` fájlban, minden feladatot külön függvényben oldj meg.

### Alapok (ismétlés)
1. Töltsd be a CSV-t, és írd ki a `shape`, `dtypes`, és a hiányzó értékek számát oszloponként.
2. Szűrj egy tetszőleges ligára és szezonra, majd számold meg a meccsek számát.
3. Rendezd a meccseket `total_goals` szerint csökkenő sorrendbe, írd ki a top 10-et.

### Új oszlopok
4. Hozz létre egy `is_draw` logikai oszlopot (`result == "D"`).
5. Hozz létre egy `high_scoring` oszlopot, ami `True`, ha `total_goals >= 4`.
6. Alakítsd `datetime`-má a `match_date` oszlopot, és hozz létre belőle egy `month` és egy
   `weekday` oszlopot.

### Csoportosítás (groupby)
7. Számold ki ligánként az átlagos `total_goals`-t és a meccsek számát egyben
   (`.agg(["mean", "count"])`).
8. Számold ki csapatonként (hazai pályán) a győzelmi arányt
   (`hazai győzelmek száma / hazai meccsek száma`).
9. Mely hónapokban (`month` oszlop a 6. feladatból) a legmagasabb az átlagos gólszám?

### Haladóbb kérdések
10. Készíts egy "forma" mutatót: egy kiválasztott csapat utolsó 5 meccsének eredményeit
    (`W`/`D`/`L`) időrendben (tipp: szűrés csapatra, rendezés dátum szerint, `.tail(5)`).
11. Pivot tábla: ligák (sorok) vs. szezonok (oszlopok), érték = átlagos `total_goals`
    (`pd.pivot_table`).
12. Mely csapatpárosok (`home_team` + `away_team`) játszottak egymás ellen a legtöbbször?
    (`value_counts` egy kombinált oszlopon).

## Tipp
Minden feladatnál írasd ki a köztes eredményt (`print`), hogy ellenőrizni tudd a logikát,
mielőtt a következő lépésre lépsz.
