import pandas as pd
import numpy as np


# Convert runtime from object to int (hours)
# Not the most elegant way, not handling edge cases, hardcoded etc. but it works for this data
def ParseRuntime(runtime_str):
    time_part = runtime_str.split("Length: ")[1]
    if len(time_part) == 4:
        hrs_part = int(time_part.split(" hr")[0])
        return hrs_part
    elif len(time_part) == 5:
        hrs_part = int(time_part.split(" hrs")[0])
        return hrs_part
    elif " hr " in time_part:
        hrs_part, mins_part = time_part.split(" hr and ")
    elif " hrs " in time_part:
        hrs_part, mins_part = time_part.split(" hrs and ")
    else:
        return np.nan

    hrs = int(hrs_part)
    mins = int(mins_part.split(" mins")[0])
    runtime = round((hrs * 60 + mins) / 60, 2)  # Convert hrs + minutes to hrs
    return runtime


## Data cleanup "Language: English" -> "English" etc.
df = pd.read_csv("../data/scraped/bastsellers_scrape.csv")
df.dtypes
df["rating"] = df["rating"].str.split(" out").str[0]
df["language"] = df["language"].str.split((" ")).str[1]
df["runtime"] = df["runtime"].apply(ParseRuntime)
# Check if there is some case where ParseRuntime doesn't work
df[df["runtime"].isna()]


df.to_csv("../data/raw/bestsellers_raw.csv", index=False)


## Formating for ploting

# By runtime
df = (  # assigning for pretty formating
    pd.read_csv("../data/raw/bestsellers_raw.csv")
    .sort_values("runtime", ascending=False)
    .loc[:, ["title", "runtime"]]
    .to_csv("../data/formated/highest_runtime.csv", index=False)
)


# Distribution, rating by runtime
df = pd.read_csv("../data/raw/bestsellers_raw.csv").loc[
    :, ["title", "rating", "runtime"]
]

df["runtime"] = df["runtime"].clip(upper=35)
bins = range(
    0, 36, 5
)  # 35 because there is one audiobook that has round 45 hrs runtime and it compresses the chart
labels = [f"{i}-{i + 5}" for i in bins[:-1]]  # 5hr bins
df["runtime_bin"] = pd.cut(
    x=df["runtime"], bins=bins, labels=labels, include_lowest=True
)

# Grouping data for chart
avg_ratings = df.groupby("runtime_bin")["rating"].mean().reset_index()
counts = df["runtime_bin"].value_counts().reindex(labels).reset_index()
counts.columns = ["runtime_bin", "count"]
df = avg_ratings.merge(counts, on="runtime_bin")
df.to_csv("../data/formated/rating_runtime_correlation.csv", index=False)
