import pandas as pd


def ReadData():
    df = pd.read_csv("../data/raw/US_births_2000-2014_SSA.csv")
    return df


def BirthsByX(index, name, *args):
    (
        ReadData()
        .loc[:, [index, "births"]]
        .groupby(index)
        .sum()
        .to_csv(f"../data/formated/{name}.csv")
    )


def ConvertAndSave(df, name):
    df["date"] = pd.to_datetime(
        df.rename(columns={"date_of_month": "day"})[["year", "month", "day"]]
    )
    df = df.loc[:, ["births", "date"]]
    df.to_csv(f"../data/formated/{name}", index=False)


# Birth count by month
BirthsByX("month", "births_by_month")

# Birth volumes across days
df = (
    ReadData()
    .loc[:, ["day_of_week", "births"]]
    .groupby("day_of_week")
    .sum()
    .reset_index()
)
weekday_map = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
df["day_of_week"] = df["day_of_week"].map(weekday_map)
df.to_csv("../data/formated/births_by_day.csv", index=False)

# Long-Term Trends
BirthsByX("year", "births_by_year")

# Peak & Low Days
df = ReadData()
df_t = df.sort_values("births", ascending=False).head(8)
df_b = df.sort_values("births", ascending=False).tail(8)
ConvertAndSave(df, "births_by_date.csv")
