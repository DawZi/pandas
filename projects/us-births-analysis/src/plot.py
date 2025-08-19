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

def LineChart(df, x, y, title, xtick_rotation, xlabel, ylabel, color=None, palette=None, hue=None):
    sns.lineplot(data=df, x=x, y=y, color=color, palette=palette, hue=hue)
    plt.title(title, fontsize=15, color="#EFF6EE", x=0.45, y=1.1, fontweight="bold")
    plt.grid(True, alpha=0.05)
    plt.xticks(rotation=xtick_rotation, fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()

def PieChart(figsize, y, donut_ammount, legend, title, title_x):
    fig,ax = plt.subplots(figsize=figsize)
    plt.pie(y,
    wedgeprops=dict(width=donut_ammount),
    colors=palette_short,
    autopct="%.2f%%",
    pctdistance=1.3,
    startangle=90,
    shadow=True,
    textprops={"weight": "bold", "fontsize": 12})
    ax.legend(legend, loc="best", bbox_to_anchor=(1.5, 0.68))
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
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


#peak low birth monthly average
births_by_month = pd.read_csv("../data/formated/births_by_month.csv")

LineChart(df=births_by_month,
          x=births_by_month["month"],
          y=round(births_by_month["births"] / 1000000, 2),
          color=palette_short[2],
          xtick_rotation=0,
          xlabel="Month",
          ylabel="Births in milions",
          title="Average births by month")


#Births by day
births_by_day = pd.read_csv("../data/formated/births_by_day.csv")
BarChart(figsize=(6, 4),
         df=births_by_day,
         x="day_of_week",
         y=(round(births_by_day["births"] / 1000000, 2)),
         palette=palette_long,
         bar_width=0.8,
         title="Average births by day of the week",
         title_x=0.38)
plt.xticks(fontweight="bold", rotation=45)
plt.yticks([])


#Weekday and weekend births distribution
births_by_day_pie = pd.read_csv("../data/formated/births_by_day.csv")
data = [births_by_day_pie.loc[0:5, ["births"]].sum().sum(), births_by_day_pie.loc[5:, ["births"]].sum().sum()]
labels = ["Weekdays", "Weekend"]

PieChart(figsize=(6, 4),
         y=data,
         donut_ammount=0.35,
         legend=labels,
         title="Weekday and weekend births distribution",
         title_x=0.54,)


#Births by year
births_by_year = pd.read_csv("../data/formated/births_by_year.csv")
LineChart(df=births_by_year,
          x="year",
          y=round(births_by_year["births"] / 1000000, 2),
          color=palette_short[2],
          xtick_rotation=0,
          xlabel="Year",
          ylabel="Births in milions",
          title="Trends in Annual Births (2000-2014)")

plt.axvline(
            x=2008, 
            color=palette_short[4], 
            linestyle="--")
plt.text(
         2008 + 0.1,
         (births_by_year["births"] / 1000000).min(),
         "Financial Crisis", 
         rotation=90,
         color=palette_short[4],
         va="bottom",
         ha="left",
         fontsize=10)


#Dates with most births
highest_births_by_date = pd.read_csv("../data/formated/births_by_date.csv").sort_values("births", ascending=False).head(8)
BarChart(figsize=(6,4),
         df=highest_births_by_date,
         x="births",
         y="date",
         palette=palette_long,
         bar_width=0.8,
         title="Dates with most births",
         title_x=0)
plt.xticks([])
plt.yticks(fontweight="bold")


#Dates with least births
lowest_births_by_date = pd.read_csv("../data/formated/births_by_date.csv").sort_values("births", ascending=False).tail(8)
BarChart(figsize=(6,4),
         df=highest_births_by_date,
         x="births",
         y="date",
         palette=palette_long,
         bar_width=0.8,
         title="Dates with least births",
         title_x=0)
plt.xticks([])
plt.yticks(fontweight="bold")


