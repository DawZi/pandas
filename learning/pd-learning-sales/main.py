import pandas as pd

df = pd.read_csv("data/data.txt", parse_dates=["purchase_date"])

# Utils
df.columns

# Total average
df.mean(numeric_only=True)


# last purchase date
last_purchase_date = df.groupby("customer_id")["purchase_date"].max()
reference_date = pd.to_datetime("2023-05-01")
recency = (reference_date - last_purchase_date).dt.days

# frequency

frequency = (
    df.groupby("customer_id")["purchase_date"].count().sort_values(ascending=False)
)

# monetary
monetary = (
    df.groupby("customer_id")
    .sum(numeric_only=True)["amount"]
    .sort_values(ascending=False)
)

# RECENCY, FREQUENCY, MONETARY DATAFRAME + CALCS
rfm_df = pd.DataFrame()
rfm_df["recency"] = recency
rfm_df["frequency"] = frequency
rfm_df["monetary"] = monetary

# Check if values ok
rfm_df

# Averages to determine score
rfm_df["recency"].mean()  # >60 = 1 | <60 = 2 | <30 = 3
rfm_df["frequency"].mean()  # <1 = 1 | 2 = 2 | >=3 =3
rfm_df["monetary"].mean()  # <325 = 1 | 325 - 405 = 2 | >405 = 3


# Recency Score
rfm_df.loc[rfm_df["recency"] <= 30, ["recency"]] = 3
rfm_df.loc[(rfm_df["recency"] < 60) & (rfm_df["recency"] > 30), ["recency"]] = 2
rfm_df.loc[rfm_df["recency"] >= 60, ["recency"]] = 1


# Frequency Score
rfm_df.loc[rfm_df["frequency"] == 1, ["frequency"]] = 1
rfm_df.loc[(rfm_df["frequency"] == 2), ["frequency"]] = 2
rfm_df.loc[rfm_df["frequency"] > 2, ["frequency"]] = 3


# Monetary Score
rfm_df.loc[rfm_df["monetary"] <= 325, "monetary"] = 1
rfm_df.loc[(rfm_df["monetary"] > 325) & (rfm_df["monetary"] < 405), ["monetary"]] = 2
rfm_df.loc[rfm_df["monetary"] >= 405, "monetary"] = 3

# Check if values are ok
rfm_df

# Score calculation
rfm_df["Total_Score"] = (
    (0.5 * rfm_df["recency"]) + (0.3 * rfm_df["frequency"]) + (0.3 * rfm_df["monetary"])
)

top_20_percent = 0.2 * rfm_df["Total_Score"].count()
# Sort by most valuable customers
rfm_df["Total_Score"].sort_values(ascending=False).head(round(top_20_percent))
