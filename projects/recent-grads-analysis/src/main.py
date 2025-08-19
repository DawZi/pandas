import pandas as pd

df = pd.read_csv("../data/raw/recent-grads.csv")

df.isnull().sum()
df = df.fillna(value=0)
df.columns

# Highest median salary
df.sort_values("Median", ascending=False)
df_median = df.loc[:, ["Major", "Median"]].sort_values("Median", ascending=False)
df_median
df_median.to_csv("../data/formated/median.csv", index=False)

# Highest unemployment rate
df_unemployment = df.loc[:, ["Major", "Unemployment_rate"]]
df_unemployment = df_unemployment.sort_values("Unemployment_rate", ascending=False)
df_unemployment
df_unemployment.to_csv("../data/formated/unemployment.csv", index=False)

# Distribution of majors by category
major_category = (
    df.groupby("Major_category")["Major"]
    .count()
    .sort_values(ascending=False)
    .to_frame()
)
major_category = pd.read_csv("../data/formated/major_category.csv")
other = major_category.iloc[5:]["Major"].sum()
filtered = major_category.iloc[:5]
major_category = pd.concat(
    [filtered, pd.DataFrame({"Major_category": ["Other"], "Major": [other]})],
    ignore_index=True,
)
major_category.to_csv("../data/formated/major_category.csv")
