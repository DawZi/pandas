import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Palette + style
rocket_cmap = sns.color_palette("rocket", as_cmap=True)
palette20 = [rocket_cmap(x) for x in np.linspace(0.3, 0.9, 20)]
sns.set_style("darkgrid")

# Highest runtime
df = pd.read_csv("../data/formated/highest_runtime.csv").head(15)

fig, ax = plt.subplots(figsize=(8, 8))
sns.barplot(
        df,
        x="runtime",
        y="title",
        palette=palette20,
        saturation= 1.1
    )
plt.title("Bestselling audiobooks with the longest runtime", fontsize=15)
plt.xlabel("Runtime in hours", fontsize=9)
plt.ylabel("")
plt.xticks(rotation=45)
plt.tight_layout()



# Distribution, rating by runtime
df = pd.read_csv("../data/formated/rating_runtime_correlation.csv")

fig, ax1 = plt.subplots(figsize=(12,6))
ax2 = ax1.twinx()
sns.barplot(data=df, x="runtime_bin", y="count", ax=ax1, alpha=0.8, color=palette20[18])
sns.lineplot(data=df, x="runtime_bin", y="rating", marker="o", ax=ax2, color=palette20[0])
ax1.set_xlabel("Runtime in hours")
ax2.set_ylabel("Average rating", color=palette20[0], fontsize=9)
ax1.set_ylabel("Number of audiobooks", color=palette20[17], fontsize=9)
plt.title("Distribution of top 100 bestselling audiobooks and their ratings by runtime", fontsize=15)
plt.tight_layout()
