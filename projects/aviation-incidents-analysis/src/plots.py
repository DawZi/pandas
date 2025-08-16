import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib.ticker import FuncFormatter
import seaborn as sns

#color palette
rocket_cmap = sns.color_palette("rocket_r", as_cmap=True)
palette = [rocket_cmap(x) for x in np.linspace(0.3, 1, 20)]

#basic barplot config
def BarPlot(df, x , y, ax):
    sns.barplot(
        x=x, 
        y=y, 
        palette=palette,
        saturation=1.1,
        ax= ax
        )


#Creates a single barplot for most or least safe airline depending on head_tail head=most tail=least
def SafetyBarChart(period, title_years, safe_least_safe, head_tail, ax):
    df = pd.read_csv("../data/formated/airline_safety.csv").sort_values(f"safety_{period}", ascending=False).reset_index(drop=True)

    if head_tail == "head":
        df = df.head(20)
    else:
        df = df.tail(20)

    BarPlot(df, y=df["airline"], x=df[f"safety_{period}"], ax=ax)
    ax.set_title(f"{safe_least_safe} airlines in years {title_years}", fontsize=30)
    ax.set_xlabel("Safety rating", fontsize=18)
    ax.set_ylabel("Airline (*regional subsidiaries are included)", fontsize=18)
    ax.set_xlim(0, 100)
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=20)
    if head_tail == "tail":
        ax.invert_yaxis()

#builds plot with 2 barplots from SafetyBarChart
def BuildSafetyPlots(config_left, config_right):
    fig, ax = plt.subplots(1, 2, figsize=(26,9))
    fig.subplots_adjust(wspace=0.5) 
    SafetyBarChart(*config_left, ax[0])
    SafetyBarChart(*config_right, ax[1])
    ax[1].set_ylabel("")


#Safest airlines
BuildSafetyPlots(("85_99", "1985-1999", "Safest", "head"),
                 ("00_14", "2000-2014","Safest", "head"))

#Least safe airlines
BuildSafetyPlots(("85_99", "1985-1999","Least safe", "tail"),
                ("00_14", "2000-2014","Least safe", "tail"))

#Incident vs fatal accident correlation
df = pd.read_csv("../data/formated/correlation.csv")

sns.scatterplot(df, x="x", y="y", hue="Years", palette=[palette[15], palette[5]], style="Years", markers='D', s=25, alpha=0.9)
plt.xlabel("Incidents")
plt.ylabel("Fatalities")
plt.title("Correlation between incidents and fatalities")
plt.tight_layout()
plt.xlim(0, 30) #Filtering one ~70 incident result that compressed whole chart


#Improvement leaders
df = pd.read_csv("../data/formated/airline_safety.csv").sort_values("safety_change", ascending=False).head(10)

fig, ax = plt.subplots()
BarPlot(df, x=df["safety_change"], y=df["airline"] , ax=ax)
ax.set_title("Safety improvement leaders", fontsize=15)
ax.set_xlabel("Positive safety rating change", fontsize=9)
ax.set_ylabel("Airline (*regional subsidiaries are included)", fontsize=9)
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)
fig.tight_layout()

#Heatmap

# Difference between periods
df = pd.read_csv("../data/formated/diff_between_periods.csv")

df["Count_norm"] =df.groupby("Metric")["Count"].transform(lambda x: x / x.max())
sns.catplot(df, kind="bar",x="Metric", y="Count_norm", hue="Years", palette=[palette[15], palette[5]])
plt.title("Relative airline safety comparison", fontsize=15)
plt.xlabel("")
plt.ylabel("Relative count (normalized)", fontsize=9)




