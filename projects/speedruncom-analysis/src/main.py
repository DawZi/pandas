import pandas as pd
import numpy as np


df = pd.read_csv("../data/raw/games-data.csv")
df.columns
df.dtypes

# Player / run count per game release year
df["nonUnixDate"] = pd.to_datetime(df["releaseDate"], unit="s").dt.year
df = (
    df.loc[:, ["runCount", "playerCount", "nonUnixDate"]]
    .groupby("nonUnixDate")
    .sum()
    .to_csv("../data/formated/count_per_year.csv")
)

# Most popular games
df = (
    df.loc[:, ["gameName", "runCount", "playerCount"]]
    .sort_values("playerCount", ascending=False)
    .pipe(
        lambda d: (
            d.to_csv("../data/formated/popular_games.csv", index=False),
            d,
        )[1]
    )
)

## Games with highest average runs per player (reusing Most popular games df therefore pipe)
df["runsPerPlayer"] = (df["runCount"] / df["playerCount"]).round(0)
df = df[(df["playerCount"] >= 5)]  # discard categories with less than 5 players

df = (
    df.sort_values("runsPerPlayer", ascending=False)
    .dropna(how="any")  # games with no runs
    .drop(["runCount", "playerCount"], axis=1)
)
df
df.to_csv("../data/formated/runs_per_player.csv", index=False)
