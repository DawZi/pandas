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


def CombineData(df):
    data1 = pd.DataFrame({
    "x": df["incidents_85_99"],
    "y": df["fatalities_85_99"],
    'Years': '1985 - 1999'
    })
    data2 = pd.DataFrame({
        "x": df["incidents_00_14"],
        "y": df["fatalities_00_14"],
        'Years': '2000 - 2014'
    })
    combined_data = pd.concat([data1, data2])
    return combined_data


#Safest airlines
BuildSafetyPlots(("85_99", "1985-1999", "Safest", "head"),
                 ("00_14", "2000-2014","Safest", "head"))

#Least safe airlines
BuildSafetyPlots(("85_99", "1985-1999","Least safe", "tail"),
                ("85_99", "1985-1999","Least safe", "tail"))

#Incident vs fatal accident correlation
df = pd.read_csv("../data/formated/airline_safety.csv")
combined_data = CombineData(df)

sns.scatterplot(combined_data, x="x", y="y", hue="Years", palette=[palette[14], palette[2]], style="Years", markers='D', s=25, alpha=0.9)
plt.xlabel("Incidents")
plt.ylabel("Fatalities")
plt.title("Correlation between incidents and fatalities")
plt.tight_layout()

#Improvement leaders
df = pd.read_csv("../data/formated/airline_safety.csv").sort_values("safety_change", ascending=False).head(10)

fig, ax = plt.subplots()
BarPlot(df, x=df["safety_change"], y=df["airline"] , ax=ax)
ax.set_title("Safety improvement leaders", fontsize=15)
ax.set_xlabel("Safety rating change", fontsize=9)
ax.set_ylabel("Airline (*regional subsidiaries are included)", fontsize=9)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"+{int(x)}"))
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)
fig.tight_layout()

#Heatmap

# Difference between periods
df = pd.read_csv("../data/formated/total_safety.csv")

df =


df = df.melt(id_vars="Years",
                  value_vars=["inc", "fat_acc", "fat"],
                  var_name="Metric",
                  value_name="Count")

df_long["Count_norm"] = df_long.groupby("Metric")["Count"].transform(lambda x: x / x.max())

g = sns.catplot(data=df_long, kind="bar",
                x="Metric", y="Count_norm", hue="Years"  )




