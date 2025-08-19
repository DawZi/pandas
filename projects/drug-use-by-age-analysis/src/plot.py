import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np


def BarChart(figsize, df, x, y, palette, bar_width, title, title_x):
    fig, ax = plt.subplots(figsize=(figsize))
    sns.barplot(df, x=x, y=y, palette=palette, width=bar_width, )
    for container in ax.containers:
        ax.bar_label(container, fontsize=9, fontweight="bold", padding=5)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.xlabel("")
    plt.ylabel("")
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

def LineChart(data, x, y, title, xtick_rotation, xlabel, ylabel, color=None, palette=None, hue=None):
    sns.lineplot(data=data, x=x, y=y, color=color, palette=palette, hue=hue)
    plt.title(title, fontsize=15, color="#EFF6EE", x=0.45, y=1.1, fontweight="bold")
    plt.grid(True, alpha=0.05)
    plt.xticks(rotation=xtick_rotation, fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
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


#Alcohol usage by age group
age_alcohol_use = pd.read_csv("../data/formated/age_group_alcohol_use.csv",)

LineChart(data=age_alcohol_use, 
          x="age", 
          y="alcohol_use",
          color=palette_short[2],
          title="Alcohol usage by age group",
          xtick_rotation=45,
          xlabel="Age",
          ylabel="People using in %")


#Marijuana vs alcohol usage
marijuana_vs_alcohol = pd.read_csv("../data/formated/marijuana_vs_alcohol_usage.csv")

LineChart(data=marijuana_vs_alcohol,
          x="age",
          y="use_percent",
          hue="drug",
          palette=[palette_short[2], palette_short[0]],
          title="Marijuana vs alcohol use trends",
          xtick_rotation=45,
          xlabel="Age",
          ylabel="Usage in %")


#Most used drug overall
most_used_drug = pd.read_csv("../data/formated/most_used_drug_overall.csv")
labels = "Alcohol", "Marijuana", "Pain releiver", "Hallucinogen", "Other"

PieChart(figsize=(6,4),
         y=most_used_drug["value"],
         donut_ammount=0.5,
         legend=labels,
         title="Most used drugs overall",
         title_x=0.2
         )


#Most using age group normalized
most_using_age = pd.read_csv("../data/formated/most_using_age_group.csv")

LineChart(data=most_using_age, 
          x="age", 
          y="total",
          color=palette_short[2],
          title="Normalized total drug use by age",
          xtick_rotation=45,
          xlabel="Age",
          ylabel="Normalized usage")
