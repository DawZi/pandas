import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec

def AddText(x, label, value):
    plt.text(x, 1, f"{label}", ha="center", fontsize=15, fontweight="bold")
    plt.text(x, 0, str(value), ha="center", fontsize=25, color="#14CC60", fontweight="bold")

def BarChart(figsize, df, x, y, palette, bar_width, title, title_x):
    fig, ax = plt.subplots(figsize=(figsize))
    sns.barplot(df, x=x, y=y, palette=palette, width=bar_width, )
    for container in ax.containers:
        ax.bar_label(container, fontsize=9, fontweight="bold")
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










#Total revenue
#Avg order value
#Total pizzas sold
#Total orders
#Average number of pizzas per order
df = pd.read_csv("../data/formated/pizza_sales.csv")
total_revenue = df["total_price"].sum()
avg_order_value = df.groupby("order_id")["total_price"].sum().mean()
total_sold = df["quantity"].sum()
total_orders = len(df.groupby("order_id"))
avg_pizzas_per_order = round(df.groupby("order_id")["quantity"].sum().mean(), 2)

plt.figure(figsize=(12,1))
plt.axis("off")
AddText(0.05, "Total revenue:", f"${total_revenue}")
AddText(0.3, "Average order value:", round(avg_order_value, 2))
AddText(0.53, "Pizzas sold:", total_sold)
AddText(0.74, "Total orders: ", total_orders)
AddText(1, "Average pizzas per order: ", avg_pizzas_per_order)
plt.tight_layout()

#Pizza sales by day
day_sales = pd.read_csv("../data/formated/day_sales.csv")

BarChart(figsize=(6, 4),
         df=day_sales,
         x="order_date",
         y="count",
         palette=palette_long,
         bar_width=1,
         title="Pizza sales by day of the week",
         title_x=0.27)
plt.yticks([])
plt.xticks(fontweight="bold", rotation=22.5)

#Hourly trend for total orders
orders_by_hour = pd.read_csv("../data/formated/orders_by_hour.csv")

xticks = np.arange(0, 24, 1)
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(orders_by_hour, x=orders_by_hour["order_time"], y=orders_by_hour["order_id"], color="#12B454")
ax.set_ylabel("Order count")
ax.set_xlabel("Order hour")
ax.set_xticks(xticks)
plt.xticks(fontweight="bold", rotation=-12.5, fontsize=9)
plt.yticks(fontweight="bold", fontsize=9)
ax.set_title("Order count by hour", fontsize=15, color="#EFF6EE", x=0.1, y=1.1, fontweight="bold")

#sales by pizza size
sales_by_size = pd.read_csv("../data/formated/sales_by_size.csv")

PieChart(figsize=(6, 4),
         y=sales_by_size["quantity"],
         donut_ammount=0.35,
         legend=sales_by_size["pizza_size"],
         title="Sales by pizza size",
         title_x=0.2)

#Sales by pizza category in % 
sales_by_category = pd.read_csv("../data/formated/sales_by_category.csv")

PieChart(figsize=(6, 4), 
         y=sales_by_category["quantity"], 
         donut_ammount=0.35, 
         legend=sales_by_category["pizza_category"], 
         title="Sales by pizza category", 
         title_x=0.31)

#Total pizza sales by category 
BarChart(figsize=(5, 3),
         df=sales_by_category,
         x="quantity",
         y="pizza_category", 
         palette=palette_short, 
         bar_width=0.5, 
         title="Total pizza sales by category", 
         title_x=0.18)
plt.xticks([])

#Top 5 best sellers by total pizzas sold
best_sellers = pd.read_csv("../data/formated/sale_numbers.csv").head(5)

BarChart(figsize=(5, 3),
         df=best_sellers,
         x="quantity",
         y="pizza_name", 
         palette=palette_short, 
         bar_width=0.5, 
         title="Best selling pizza", 
         title_x=-0.51)
plt.xticks([])

#Top 5 worst sellers by total pizzas sold
worst_sellers = pd.read_csv("../data/formated/sale_numbers.csv").head(5).sort_values(by="quantity")

BarChart(figsize=(5, 3),
         df=worst_sellers,
         x="quantity",
         y="pizza_name", 
         palette=palette_short, 
         bar_width=0.5, 
         title="Worst selling pizza", 
         title_x=-0.45)
plt.xticks([])




