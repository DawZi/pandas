import pandas as pd


def ReadData():
    df = pd.read_csv("../data/raw/airline-safety.csv")
    return df


def RatePerBil(df, col):
    return df[col] / (df["avail_seat_km_per_week"] / 1_000_000_000)


def SafetyRating(df, period):
    incident_rate = RatePerBil(df, f"incidents_{period}")
    fatal_accidents = RatePerBil(df, f"fatal_accidents_{period}")
    fatalities = RatePerBil(df, f"fatalities_{period}")

    safety_score = (incident_rate * 1) + (fatal_accidents * 5) + (fatalities * 0.1)

    return ((1 - (safety_score / safety_score.max())) * 100).round(2)


## airline Safety Rating / Improvement
df = ReadData()

# calculate safety rating based on a simple formula | change from low = better to high = better | normalize to 100
for period in ["85_99", "00_14"]:
    df[f"safety_{period}"] = SafetyRating(df, period)

df["safety_change"] = df["safety_00_14"] - df["safety_85_99"]
df.to_csv("../data/formated/airline_safety.csv", index=False)


## fatality rate per avail_seat_km_per_week per airline
df = ReadData().loc[
    :, ["airline", "avail_seat_km_per_week", "fatalities_85_99", "fatalities_00_14"]
]

# fatality rate per bilion km's
for period in ["85_99", "00_14"]:
    df[f"fatalities_per_bil_{period}"] = RatePerBil(df, f"fatalities_{period}").round(2)
df["total"] = df["fatalities_per_bil_85_99"] + df["fatalities_per_bil_00_14"]
df.to_csv("../data/formated/fatality_rate.csv")

## global safety totals
df = ReadData()
df = df.drop("airline", axis=1)
df = pd.DataFrame([df.sum()]).to_csv("../data/formated/total_safety.csv")

##Correlation data
df = pd.read_csv("../data/formated/airline_safety.csv")
data1 = pd.DataFrame(
    {"x": df["incidents_85_99"], "y": df["fatalities_85_99"], "Years": "1985 - 1999"}
)
data2 = pd.DataFrame(
    {"x": df["incidents_00_14"], "y": df["fatalities_00_14"], "Years": "2000 - 2014"}
)
combined_data = pd.concat([data1, data2])


##Difference between periods
df = pd.read_csv("../data/formated/total_safety.csv")
df = pd.DataFrame(
    {
        "Years": ["1985 - 1999", "2000 - 2014"],
        "inc": [df.loc[0, "incidents_85_99"], df.loc[0, "incidents_00_14"]],
        "fat_acc": [
            df.loc[0, "fatal_accidents_85_99"],
            df.loc[0, "fatal_accidents_00_14"],
        ],
        "fat": [df.loc[0, "fatalities_85_99"], df.loc[0, "fatalities_00_14"]],
    }
)
df = df.melt(
    id_vars="Years",
    value_vars=["inc", "fat_acc", "fat"],
    var_name="Metric",
    value_name="Count",
)
df.to_csv("../data/formated/diff_between_periods.csv")
