import pandas as pd


def ReadData():
    df = pd.read_csv("../data/raw/US_births_2000-2014_SSA.csv")
    df
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


# Peak / low birth counts by month
BirthsByX("month", "births_by_month")

# Birth volumes across weekdays vs. weekends
BirthsByX("day_of_week", "births_by_day")

# Long-Term Trends
BirthsByX("year", "births_by_year")

# Peak & Low Days
df = ReadData()
df_t = df.sort_values("births", ascending=False).head(8)
df_b = df.sort_values("births", ascending=False).tail(8)
ConvertAndSave(df_t, "highest_births_by_date.csv")
ConvertAndSave(df_b, "lowest_births_by_date.csv")
