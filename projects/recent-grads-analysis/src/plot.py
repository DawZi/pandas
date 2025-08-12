import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# Function to add value labels on top of bars


# Top 10 majors by median salary:

df = pd.read_csv("../data/formated/median.csv")
df = df.head(10)
df.columns
major = df["Major"]
median = df["Median"]
style.use("ggplot")


plt.figure(figsize=(6, 4))
plt.barh(major, median, height=0.75, color="#7289DA", edgecolor="#23272A")
plt.gca().invert_yaxis()
plt.xticks(color="#23272A")
plt.yticks(color="#23272A")
plt.title("Top 10 majors by median salary", color="#23272A", ha="right")
plt.xlabel("Median yearly income in USD", color="#23272A", fontsize=7)
for index, value in enumerate(median):
    plt.text(
        value / 2,
        index,
        str(f"${value}"),
        va="center",
        ha="center",
        color="#FFFFFF",
        fontsize=8,
    )

# Top 10 majors with highest unemployment
df = pd.read_csv("../data/formated/unemployment.csv")
df = df.head(10)
df.columns
df.dtypes
major = df["Major"]
rate = df["Unemployment_rate"].round(2)


plt.figure(figsize=(6, 4))
plt.barh(major, rate, height=0.75, color="#7289DA", edgecolor="#23272A")
plt.gca().invert_yaxis()
plt.xticks(color="#23272A")
plt.yticks(color="#23272A")
plt.title("Top 10 majors with highest unemployment", color="#23272A", ha="right")
plt.xlabel("Unemployment rate", color="#23272A", fontsize=7)
for index, value in enumerate(rate):
    plt.text(
        value / 2,
        index,
        str(value),
        va="center",
        ha="center",
        color="#FFFFFF",
        fontsize=8,
    )

# Distribution of majors by category.
df = pd.read_csv("../data/formated/major_category.csv")
df

other_sum = df.iloc[5:16]["Major"].sum()
df_filtered = df.iloc[0:5]

df_filtered = pd.concat(
    [df_filtered, pd.DataFrame({"Major_category": ["Other"], "Major": [other_sum]})],
    ignore_index=True,
)

df = df_filtered
ratio = df["Major"]
labels = df["Major_category"]

fig, ax = plt.subplots()
ax.pie(
    ratio,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#5B6DC8", "#7289DA", "#8A9DE2", "#A3B1EA", "#BCC5F0", "#D5D9F6"],
)
