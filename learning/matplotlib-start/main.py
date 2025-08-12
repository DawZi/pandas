import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100
plt.scatter(x_data, y_data, c="#329010", marker="o", s=150, alpha=0.3)

years = [2006 + x for x in range(16)]
weihts = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]
plt.plot(years, weihts, c="red", lw=2, linestyle="--")

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]
plt.bar(x, y, color="gray", align="center", width=0.1, edgecolor="black")

ages = np.random.normal(20, 1.5, 1000)
plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()], cumulative=True)

languages = ["C++", "C#", "Python", "Java", "Go"]
votes = [20, 50, 140, 1, 45]
plt.pie(
    votes,
    labels=languages,
    explode=[0, 0, 0, 0.1, 0],
    autopct="%.2f%%",
    pctdistance=0.5,
    startangle=90,
)

height = np.random.normal(172, 8, 300)
plt.boxplot(height)
