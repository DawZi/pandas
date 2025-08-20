import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

def GroupByX(group_by, csv):
    (df.groupby(group_by)
        .count()
        .reset_index()
        .loc[:, [group_by, "Sale Amount"]]
        .to_csv(f"../data/formated/{csv}.csv", index=False)
    )

#Import
df = pd.read_csv("../data/raw/Real_Estate_Sales_2001-2022_GL.csv")

# Sales Over Time 
GroupByX("List Year", "sales_per_year")

# Top 10 Towns by Total Sales Volume
GroupByX("Town", "town_sales")

# Sale Amount vs. Assessed Value
low_x, high_x = df['Assessed Value'].quantile([0.01, 0.99])
low_y, high_y = df['Sale Amount'].quantile([0.01, 0.99])

sale_vs_assessed = df[
    (df['Assessed Value'] >= low_x) & 
    (df['Assessed Value'] <= high_x) &
    (df['Sale Amount'] >= low_y) & 
    (df['Sale Amount'] <= high_y)
].loc[:, ["Assessed Value", "Sale Amount"]].to_csv("../data/formated/sale_vs_assessed.csv", index=False)