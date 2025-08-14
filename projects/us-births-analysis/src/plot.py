import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns



def Load(filename):
    df = pd.read_csv(f"../data/formated/{filename}")
    return df


def FinalizePlot(title, xlabel, ylabel):
    sns.set_style="darkgrid"
    plt.tight_layout()
    plt.title(f"{title}", fontsize=18)
    plt.xlabel(f"{xlabel}", fontsize=10)
    plt.ylabel(f"{ylabel}", fontsize=10)


def BarPlot(df, x , y):
    sns.barplot(
        x=x, 
        y=y, 
        palette=palette,
        saturation=1.1
        )



#color palette
rocket_cmap = sns.color_palette("rocket_r", as_cmap=True)
palette = [rocket_cmap(x) for x in np.linspace(0.3, 1, 10)]


#peak low birth monthly average
df = Load("births_by_month.csv")
sns.lineplot(df, x=df["month"], y=df["births"] / 1000000, color=palette[5])
FinalizePlot("Average births by month in 2000 - 2014", "Month", "Births (milions)")

#Weekly Patterns
df = Load("births_by_day.csv")
BarPlot(df, df["day_of_week"], df["births"] / 1000000)
FinalizePlot("Average births by day of the week in 2000 - 2014", "Day", "Births (milions)")

#Pie chart weekday vs weekend
df= Load("births_by_day.csv")
data = [df.loc[0:5, ["births"]].sum().sum(), df.loc[5:6, ["births"]].sum().sum()]
labels = ["Weekdays", "Weekend"]

fig, ax = plt.subplots()

wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    colors=palette[6:8],
    startangle=90,
    autopct="%.0f%%",
    textprops={"color": "white",},
    wedgeprops=dict(width=0.5),
    shadow=True,
    pctdistance=0.739

)
ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Birth volumes across the week", fontsize=18)

#Long-Term Trends
df = Load("births_by_year.csv")

sns.lineplot(df, x=df["year"], y=df["births"] / 1000000, color=palette[8])
plt.axvline(
            x=2008, 
            color=palette[1], 
            linestyle="--"
           )
plt.text(
         2008 + 0.1,
         (df["births"] / 1000000).min(),
         "Financial Crisis", 
         rotation=90,
         color=palette[1],
         va="bottom",
         ha="left",
         fontsize=10
        )

FinalizePlot("Average births by year in 2000 - 2014", "Year", "Births (milions)")

#Dates with most births
df = Load("highest_births_by_date.csv")
BarPlot(df, x=df["births"], y=df["date"])
FinalizePlot("Days with most births", "Births", "")

#Dates with least births
df = Load("lowest_births_by_date.csv")
BarPlot(df, x=df["births"], y=df["date"])
FinalizePlot("Days with least births", "Births", "")


