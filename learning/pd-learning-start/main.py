import pandas as pd
import re

df = pd.read_csv("data/raw/pokemon_data.csv")

# df_xlsx = pd.read_excel('data/raw/pokemon_data.xlsx')

# df_txt = pd.read_csv('data/raw/pokemon_data.txt', delimiter='\t')

# df_xlsx.head(3))

##Name of headers
df.columns

##Print silgle column [top 5 results]
df["Name"][0:5]

##print multiple columns [top 5 results]
df[["Name", "HP"]][0:5]

##Read Any Row ()
df.iloc[1:4]

##Read specific location(Row, Column)
df.iloc[2, 1]

##Iterate over rows
for index, row in df.iterrows():
    print(index, row["Name"])

##All things in specific column name and multiple column names
df.loc[df["Type 1"] == "Grass"]
new_df = df.loc[
    (df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)
]

##Reset index numeration
new_df = new_df.reset_index(drop=True)

## Sort values asc or desc
df.sort_values(["Name", "HP"], ascending=[1, 0])

##Drop a column
df = df.drop(columns=["Total"])

##Add column / sum columns
df["Total"] = (
    df["HP"]
    + df["Attack"]
    + df["Defense"]
    + df["Sp. Atk"]
    + df["Sp. Def"]
    + df["Speed"]
)

##Faster way
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
df.sort_values(["Total"], ascending=False).head(5)

##Get columns
cols = list(df.columns)

##Move column
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# df = df[["Total", "Hp", "Defence", ...]]

##Save file
df.to_csv("data/formated/pokemon_data_formated.csv", index=False)

##Exclude column ~ To inverse (show only ones that dont contain)
df.loc[df["Name"].str.contains("Mega")]

##Regex
df.loc[df["Type 1"].str.contains("Fire|Grass", flags=re.I, regex=True)]

##Starting with "pi"
df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)]

##Change value of all rows with this name
df.loc[df["Type 1"] == "Flame", "Type 1"] = "Fire"

##Change value of different column using value
df.loc[df["Type 1"] == "Fire", ["Legendary"]] = True

##Some random ops
new_df = df.loc[(df["Total"] > 600) & (~df["Name"].str.contains("Mega"))]
new_df = new_df.reset_index(drop=True)
new_df = new_df.sort_values(["Total"], ascending=False)
new_df.loc[new_df["Legendary"] == False]  # noqa: E712

##Aggregate statistics .sum .mean . count
df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("HP", ascending=False)

##Track how many times event accurs in dataframe or simple how many of something there is
df["count"] = 1
df.groupby(["Type 1"]).count()["count"]

##Cleanup
df = df.drop(columns="count")

##Big DATASETS; chunksize = ammount of rows

# print a chunk of df
for df in pd.read_csv("data/raw/pokemon_data.csv", chunksize=100):
    print("ChunkDF")
    print(df)

new_df = pd.DataFrame(columns=df.columns)

# Save results of query as 'results'
for df in pd.read_csv("data/raw/pokemon_data.csv", chunksize=100):
    results = df.groupby(["Type 1"]).count()

# append to table
new_df = pd.concat([new_df, results])
new_df.sort_values(["Type 1"])
