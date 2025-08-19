import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

def BarChart(figsize, df, x, y, palette, bar_width, title, title_x):
    fig, ax = plt.subplots(figsize=(figsize))
    sns.barplot(df, x=x, y=y, palette=palette, width=bar_width, )
    for container in ax.containers:
        ax.bar_label(container, fontsize=9, fontweight="bold", padding=5)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.xlabel("")
    plt.ylabel("")
    plt.tight_layout()

#Styling and palette
custom_colors = ["#2C2C34"]
palette_short = ["#064D26", "#0A7734", "#12B454", "#4FD07D", "#A5F0C5"]
palette_long = ["#0F9948", "#10A34D", "#11AD52", "#12B856", "#13C25B", "#14CC60", "#20CF68", "#2CD170", "#37D478", "#43D680"]
sns.set_style(rc={"figure.facecolor": "#2C2C34",
                  "axes.labelcolor": "#14CC60",
                  "xtick.direction": "out",
                  "ytick.direction": "out",
                  "xtick.color": "#EFF6EE",
                  "ytick.color": "#EFF6EE",
                  "axes.axisbelow": True,
                  "grid.linestyle": "-",
                  "text.color": "#EFF6EE",
                  "lines.solid_capstyle": "round",
                  "patch.edgecolor": "w",
                  "patch.force_edgecolor": False,
                  "patch.edgecolor":"#EFF6EE",
                  "axes.grid": False,
                  "axes.facecolor": "#2C2C34",
                  "axes.spines.right": False, 
                  "axes.spines.left": False,
                  "axes.spines.top": False,
                  "axes.spines.bottom": False
                  })


# Highest runtime
highest_runtime = pd.read_csv("../data/formated/highest_runtime.csv").head(8)

BarChart(figsize=(6,4),
         df=highest_runtime,
         x="runtime",
         y="title",
         palette=palette_long,
         bar_width=0.8,
         title="Bestselling audiobooks with the longest runtime",
         title_x=0.2)
plt.xlabel("Runtime in hours")



# Distribution, rating by runtime
df = pd.read_csv("../data/formated/rating_runtime_correlation.csv")

fig, ax1 = plt.subplots(figsize=(6,4))
ax2 = ax1.twinx()
sns.barplot(data=df, x="runtime_bin", y="count", ax=ax1, color=palette_short[1])
sns.lineplot(data=df, x="runtime_bin", y="rating", marker="o", ax=ax2, color=palette_short[4])
ax1.set_xlabel("Runtime in hours")
ax2.set_ylabel("Average rating", color=palette_short[4], fontsize=9)
ax1.set_ylabel("Number of audiobooks", color=palette_short[1], fontsize=9)
plt.title("Bestselling audiobooks and their ratings by runtime", fontsize=15, color="#EFF6EE", y=1.1, fontweight="bold")
plt.tight_layout()
