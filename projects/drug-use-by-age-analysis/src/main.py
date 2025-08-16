import pandas as pd
import numpy as np


# Most commonly used drug overall
df = pd.read_csv("../data/raw/drug-use-by-age.csv")
df = (
    df.drop(columns=["age", "n"])
    .replace("-", np.nan)
    .astype("float")
    .filter(regex="_use", axis=1)
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
df.columns = ["drug", "value"]
df_1 = df.loc[:4].copy()  # Group low usage drugs into single category called other
df_2 = df.loc[5:].copy()
other_value = df_2["value"].sum()
df_other = pd.DataFrame([["Other", other_value]], columns=df.columns)
df = pd.concat([df_1, df_other], ignore_index=True)
df.to_csv("../data/formated/most_used_drug_overall.csv", index=False)

# Age group ranking by alcohol use
df = (
    pd.read_csv("../data/raw/drug-use-by-age.csv")
    .loc[:, ["age", "alcohol_use"]]
    .to_csv("../data/formated/age_group_alcohol_use.csv", index=False)
)

# Marijuana va alcohol use trends
df = (
    pd.read_csv("../data/raw/drug-use-by-age.csv")
    .loc[:, ["age", "marijuana_use", "alcohol_use"]]
    .rename(columns={"marijuana_use": "Marijuana use", "alcohol_use": "Alcohol use"})
    .melt(id_vars="age", var_name="drug", value_name="use_percent")
    .to_csv("../data/formated/marijuana_vs_alcohol_usage.csv", index=False)
)

# Highest using age group
df = pd.read_csv("../data/raw/drug-use-by-age.csv")
df_1 = df.loc[:, ["age"]]
df_2 = df.filter(regex="_use", axis=1).T.sum()
df_2 = pd.DataFrame(df_2).rename(columns={0: "total"})
df = df_1.join(df_2, how="inner")
# normalize 0-1range

df["total"] = (df["total"] - df["total"].min()) / (
    df["total"].max() - df["total"].min()
)
df.to_csv("../data/formated/most_using_age_group.csv", index=False)
