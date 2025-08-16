import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np

#Palette + style
rocket_cmap = sns.color_palette("rocket", as_cmap=True)
palette20 = [rocket_cmap(x) for x in np.linspace(0.3, 0.9, 20)]
palette10 = [rocket_cmap(x) for x in np.linspace(0.3, 0.9, 10)]
sns.set_style("darkgrid")

#Alcohol usage by age group
df = pd.read_csv("../data/formated/age_group_alcohol_use.csv",)

fig, ax = plt.subplots(figsize=(8, 8))
sns.barplot(
        df,
        x="age",
        y="alcohol_use",
        palette=palette20,
        saturation= 1.1
    )
plt.title("Alcohol usage by age group", fontsize=15)
plt.xlabel("Age", fontsize=9)
plt.ylabel("Alcohol usage %", fontsize=9)
plt.xticks(rotation=45)
plt.tight_layout()


#Marijuana vs alcohol usage
df = pd.read_csv("../data/formated/marijuana_vs_alcohol_usage.csv")
        
fig, ax = plt.subplots(figsize=(10,8))
sns.lineplot(df, x="age", y="use_percent",hue="drug" ,palette=[palette20[2], palette20[14]])
plt.xlabel("Age", fontsize=9)
plt.ylabel("Usage in %", fontsize=9)
plt.title("Marijuana vs alcohol use trends", fontsize=15)
plt.xticks(rotation=45)
plt.tight_layout()


#Most used drug overall
df = pd.read_csv("../data/formated/most_used_drug_overall.csv")

values = df["value"]
labels = "Alcohol", "Marijuana", "Pain releiver", "Hallucinogen", "Tranquilizer", "Other"

fig, ax = plt.subplots(figsize=(8,8))
plt.pie(
        values, 
        labels=labels, 
        colors=palette10[1:7], 
        autopct="%1.1f%%", 
        textprops={"color": "white"},
        shadow=True
)
ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Most common drugs", fontsize=15)
plt.tight_layout()


#most using age group normalized
df = pd.read_csv("../data/formated/most_using_age_group.csv")

fig, ax = plt.subplots(figsize=(10,8))
sns.lineplot(df, x="age", y="total" ,color=palette10[1])
plt.xlabel("Age", fontsize=9)
plt.ylabel("Normalized usage", fontsize=9)
plt.title("Normalized total drug use by age", fontsize=15)
plt.xticks(rotation=45)
plt.tight_layout()
