import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline  
import seaborn as sns

def BarChart(data, x, y, xlabel, ylabel, title):
    sns.set_theme(style="darkgrid")
    sns.barplot(data, x=x, y=y, palette="rocket")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, loc="center", fontsize=18)
    plt.tight_layout()

# Games with highest average runs per player
df = pd.read_csv("../data/formated/runs_per_player.csv").head(15)
BarChart(df, "runsPerPlayer", "gameName", "Runs per player", "", "Games with most runs per player")

# Most popular games
##By player count
df = pd.read_csv("../data/formated/popular_games.csv").head(10)
BarChart(df, "playerCount", "gameName", "Player count", "", "Games with most players")

##By run count
df = df.sort_values("runCount", ascending=False).reset_index(drop=True)
BarChart(df, "runCount", "gameName", "Player count", "", "Games with most submitted runs")

# Player / run count per game release year
df = pd.read_csv("../data/formated/count_per_year.csv").head(51).rename(columns={"runCount" : "Runs"}) #data from only 50 years of game releases is complete

cmap = sns.color_palette("rocket", as_cmap=True)
g = sns.relplot(
    data=df,
    x="nonUnixDate", y="playerCount",
    hue="Runs", size="Runs",
    palette=cmap, sizes=(10, 200),
)

plt.title("Player count per game release year", fontsize=15)
plt.ylabel("Player number")
plt.xlabel("Year")