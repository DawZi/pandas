import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import seaborn as sns


def BarChart(figsize, df, x, y, palette, bar_width, title, title_x):
    fig, ax = plt.subplots(figsize=(figsize))
    sns.barplot(
        df,
        x=x,
        y=y,
        palette=palette,
        width=bar_width,
    )
    for container in ax.containers:
        ax.bar_label(container, fontsize=9, fontweight="bold", padding=5)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.xlabel("")
    plt.ylabel("")
    plt.tight_layout()


def PieChart(figsize, y, donut_ammount, legend, legend_bbox, title, title_x):
    fig, ax = plt.subplots(figsize=figsize)
    plt.pie(
        y,
        wedgeprops=dict(width=donut_ammount),
        colors=palette_short,
        autopct="%.2f%%",
        pctdistance=1.3,
        startangle=90,
        shadow=True,
        textprops={"weight": "bold", "fontsize": 12},
    )
    ax.legend(legend, loc="best", bbox_to_anchor=legend_bbox)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.tight_layout()


# Styling and palette
custom_colors = ["#2C2C34"]
palette_short = ["#064D26", "#0A7734", "#0F9948", "#12B454", "#4FD07D", "#A5F0C5"]
palette_long = [
    "#0F9948",
    "#10A34D",
    "#11AD52",
    "#12B856",
    "#13C25B",
    "#14CC60",
    "#20CF68",
    "#2CD170",
    "#37D478",
    "#43D680",
]
sns.set_style(
    rc={
        "figure.facecolor": "#2C2C34",
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
        "patch.edgecolor": "#EFF6EE",
        "axes.grid": False,
        "axes.facecolor": "#2C2C34",
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.top": False,
        "axes.spines.bottom": False,
    }
)


# Top majors by median salary:
median = pd.read_csv("../data/formated/median.csv").head(10)

BarChart(
    figsize=(8, 4),
    df=median,
    x="Median",
    y="Major",
    palette=palette_long,
    bar_width=0.8,
    title="Most earning majors",
    title_x=-0.6,
)
plt.xticks([])


# Top 10 majors with highest unemployment
highest_unemplotyment = (
    pd.read_csv("../data/formated/unemployment.csv").head(10).round(2)
)

BarChart(
    figsize=(8, 4),
    df=highest_unemplotyment,
    x="Unemployment_rate",
    y="Major",
    palette=palette_long,
    bar_width=0.8,
    title="Majors with highest unemployment rate",
    title_x=-0.37,
)
plt.xticks([])


# Distribution of majors by category.
major_category = pd.read_csv("../data/formated/major_category.csv")

PieChart(
    figsize=(8, 4),
    y=major_category["Major"],
    donut_ammount=0.35,
    legend=major_category["Major_category"],
    legend_bbox=(1.2, 0.74),
    title="Majors distribution by category",
    title_x=0.57,
)
