import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import matplotlib.colors as col
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
cmap = col.LinearSegmentedColormap.from_list("green_cmap", palette_short)

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

# Games with highest average runs per player
runs_per_player = pd.read_csv("../data/formated/runs_per_player.csv").head(10)

BarChart(figsize=(6, 4), 
         df=runs_per_player, 
         x="runsPerPlayer", 
         y="gameName", 
         palette=palette_long, 
         bar_width=0.8, 
         title="Games with most runs per player", 
         title_x=-0.14)
plt.xticks([])
# Most popular games
##By player count
most_popular_games = pd.read_csv("../data/formated/popular_games.csv").head(10)

BarChart(figsize=(6, 4), 
         df=most_popular_games, 
         x="playerCount", 
         y="gameName",
         palette=palette_long, 
         bar_width=0.8, 
         title="Games with highest ammount of players", 
         title_x=-0.19)
plt.xticks([])

##By run count
run_count = pd.read_csv("../data/formated/popular_games.csv").sort_values("runCount", ascending=False).reset_index(drop=True).head(10)

BarChart(figsize=(6, 4), 
         df=run_count, 
         x="runCount", 
         y="gameName", 
         palette=palette_long, 
         bar_width=0.8, 
         title="Games with most submitted runs", 
         title_x=-0.06)
plt.xticks([])

# Player / run count per game release year
df = pd.read_csv("../data/formated/count_per_year.csv").head(51).rename(columns={"runCount" : "Runs"}) #data from only 50 years of game releases is complete

plot = sns.relplot(
    data=df,
    x="nonUnixDate", 
    y="playerCount",
    hue="Runs", 
    size="Runs",
    palette=cmap, 
    sizes=(10, 200),
    height=4,
    aspect=6/4,

)
sns.despine(left=True, bottom=True)
plt.grid(True, alpha=0.1)
plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")
plt.ylabel("Player count")
plt.xlabel("Date")
plt.title("Player count per game release year", fontsize=15, color="#EFF6EE", x=0.5, y=1.1, fontweight="bold")
