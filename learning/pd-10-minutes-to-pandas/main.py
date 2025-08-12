import numpy as np
import pandas as pd

# Series creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# dataframe passing array
dates = pd.date_range("20130101", periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

# dataframe passing dictionary
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": "foo",
    }
)

df2
df2.dtypes

# Viewing data
df.head()  # Top rows
df.tail(3)  # Bottom rows
df.index  # Row labels
df.columns  # Column labels
df.to_numpy()  # Numpy representation without index or column
df.describe()  # Quick statistic summary
df.T  # Transporting data (Swap index with columns visually)
df.sort_index(axis=1, ascending=False)  # Sort by axis
df.sort_values(by="B")  # Sort values

# Selection
df["A"]  # Select a column and yields a series [""]
df[0:3]  # : selects matching rows
df.loc[:, ["A", "B"]]  # Select by column labels
df.loc["20130102":"20130104", ["A", "B"]]  # Select by column labels within range
df.loc[dates[0], "A"]  # Select single row and column label
df.at[dates[0], "A"]  # Equivalent to previous method

# Selection by position
df.iloc[3]  # Selection via passed intiger position
df.iloc[3:5, 0:2]  # Int slices (row, column)
df.iloc[[1, 2, 4], [0, 2]]  # List of int positions
df.iloc[1:3, :]  # Slicing rows
df.iloc[:, 1:3]  # Slicing columns
df.iloc[1, 1]  # Getting specific value
df.iat[1, 1]  # Equivalent of previous method

# Bool indexing
df[df["A"] > 0]  # Rows where df.A Greater than 0
df[df > 0]  # Selecting values where bool condition is met

##isin() for filtering
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2
df2[df2["E"].isin(["two", "four"])]

# Setting
##new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df["F"] = s1

df.at[dates[0], "A"] = 0  # Setting values by label
df.iat[0, 1] = 0  # Setting values by position
df.loc[:, "D"] = np.array([5] * len(df))  # Setting by assigning a numpy array

# Where operation with setting
df2 = df.copy()
df2[df2 > 0] = -df2
df2

# Missing data
##change/add/delete the index on a specified axis
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1

df1.dropna(how="any")  # drops any rows that have missing data
df1.fillna(value=5)  # fills missing data
pd.isna(df1)  # If values are nan = False, else True

# Operations
##Stats
df.mean()  # mean value for each column
df.mean(axis=1)  # mean value for each row

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
df.sub(s, axis="index")

##User defined functions
df.agg(lambda x: np.mean(x) * 5.6)
df.transform(lambda x: x * 101.2)

##Value Counts
s = pd.Series(np.random.randint(0, 7, size=10))
s
s.value_counts()  # count the number of times value exists in df

##String methods
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower()

# Merge
##Concat
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]  # break df into pieces
pd.concat(pieces)  # Concatenating pandas objects together row-wise

##Join
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "lval": [4, 5]})

pd.merge(left, right, on="key")

###merge on unique keys
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "lval": [4, 5]})

pd.merge(left, right, on="key")
