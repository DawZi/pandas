import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline  
import seaborn as sns

def BarChart(figsize, df, x, y, palette, bar_width, title, title_x, percent=False):
    fig, ax = plt.subplots(figsize=(figsize))
    sns.barplot(df, x=x, y=y, palette=palette, width=bar_width, )
    if percent == True: 
        for container in ax.containers:
            ax.bar_label(container, fmt="%.2f%%", fontsize=9, fontweight="bold", padding=5)
    else:
        for container in ax.containers:
            ax.bar_label(container, fontsize=9, fontweight="bold", padding=5)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.xlabel("")
    plt.ylabel("")
    plt.tight_layout()

def LineChart(df, x, y, title, xtick_rotation, xlabel, ylabel, color=None, palette=None, hue=None):
    sns.lineplot(df=data, x=x, y=y, color=color, palette=palette, hue=hue)
    plt.title(title, fontsize=15, color="#EFF6EE", x=0.45, y=1.1, fontweight="bold")
    plt.grid(True, alpha=0.05)
    plt.xticks(rotation=xtick_rotation, fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()

def PieChart(figsize, y, donut_ammount, legend, title, title_x, bbox):
    fig,ax = plt.subplots(figsize=figsize)
    plt.pie(y,
    wedgeprops=dict(width=donut_ammount),
    colors=palette_short,
    autopct="%.2f%%",
    pctdistance=1.3,
    startangle=90,
    shadow=True,
    textprops={"weight": "bold", "fontsize": 12})
    ax.legend(legend, loc="best", bbox_to_anchor=bbox)
    plt.title(title, fontsize=15, color="#EFF6EE", x=title_x, y=1.1, fontweight="bold")
    plt.tight_layout()

#Styling and palette
custom_colors = ["#2C2C34"]
palette_short = ["#04351A" ,"#064D26", "#0A7734", "#12B454", "#4FD07D", "#A5F0C5"]
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

pd.read_csv("../data/urbanization-index-2022.csv")
#most rural districts
most_rural = pd.read_csv("../data/urbanization-index-2022.csv").sort_values("rural", ascending=False).head(10)
BarChart(figsize=(6, 4),
         df=most_rural,
         x=round(most_rural["rural"], 2),
         y="stcd",
         palette=palette_long,
         bar_width=0.8,
         title="Most rural districts",
         title_x=0.1,
         percent=True)

#distribution of districts by group
districts_group = pd.read_csv("../data/urbanization-index-2022.csv").loc[:, ["grouping", "cd"]].groupby("grouping").count().reset_index()
order = [1, 5, 0, 4, 3, 2]
districts_group = districts_group.iloc[order].reset_index(drop=True)

PieChart(figsize=(6,4),
         y=districts_group["cd"],
         donut_ammount=0.35,
         legend=districts_group["grouping"],
         title="Distribution of districts by group",
         title_x=0.5,
         bbox=(1.2, 0.8))

