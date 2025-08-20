import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
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
palette_short = ["#064D26", "#0A7734", "#12B454", "#4FD07D", "#A5F0C5"]
palette_long = ["#0F9948", "#10A34D", "#11AD52", "#12B856", "#13C25B", "#14CC60", "#20CF68", "#2CD170", "#37D478", "#43D680"]
palette_tree = ["#12B856", "#10A64A", "#0E9440", "#0C8236", "#0A712D", "#085F24", "#064E1B", "#043D12", "#022C0A", "#011A03", "#000900"]
cmap = ListedColormap(palette_short)

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


# Sales Per Year #Line
sales_per_year = pd.read_csv("../data/formated/sales_per_year.csv")

LineChart(data=sales_per_year,
          x=sales_per_year["List Year"],
          y=sales_per_year["Sale Amount"],
          title="Real estate sales by year",
          xtick_rotation=45,
          xlabel="",
          ylabel="Total sales",
          color=palette_long[2])
plt.xticks(ticks=sales_per_year["List Year"].unique())


# Top 10 Towns by Total Sales Volume #Bar
top_10 = pd.read_csv("../data/formated/town_sales.csv").sort_values("Sale Amount", ascending=False).head(10)

BarChart(figsize=(6,4),
         df=top_10,
         x=top_10["Sale Amount"],
         y=top_10["Town"],
         palette=palette_long,
         bar_width=1,
         title="Top towns by sale volume",
         title_x=0.45
         )
plt.xticks([])


# Sale Amount vs. Assessed Value #Heatmap or sum shit
sale_vs_assessed = pd.read_csv("../data/formated/sale_vs_assessed.csv")

plt.figure(figsize=(10, 6))
plt.hexbin(
    sale_vs_assessed['Assessed Value'] / 10000,
    sale_vs_assessed['Sale Amount'] / 10000,
    gridsize=50,
    cmap=cmap,
    bins='log'
)
plt.colorbar(label='Number of properties')
plt.xlabel('Assessed value in thousands')
plt.ylabel('Sale vmount in thousands')
plt.title('Density of assessed value vs sale amount', fontsize=15, y=1.1, fontweight="bold")
plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")
