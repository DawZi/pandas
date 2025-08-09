import pandas as pd

df = pd.read_csv("data/procesed/RampartVehicleThefts.csv")

# Separate quater df's for comparassion
df_Q3 = pd.DataFrame(df.loc[df["quater"] == "2024Q3"])
df_Q4 = pd.DataFrame(df.loc[df["quater"] == "2024Q4"])

# Just some cleanup
df_Q3 = df_Q3.reset_index(drop=True)
df_Q4 = df_Q4.reset_index(drop=True)

# Total investigations launched
df_Q4["count"].count()

# Difference in number of vehicle thefts between this and prev quater
total_vehicle_thefts_diff = df_Q3["count"].count() - df_Q4["count"].count()

# Status converted to percentages Q3
Q3Status = df_Q3.groupby("Status Desc")["count"].count()
Q3Status_per = round(Q3Status / len(df_Q3) * 100, 2)

# Status converted to percentages Q4
Q4Status = df_Q4.groupby("Status Desc")["count"].count()
Q4Status_per = round(Q4Status / len(df_Q4) * 100, 2)

# Difference
num_diff = Q4Status - Q3Status
num_diff_per = Q4Status_per - Q3Status_per

# Most common times for stealing with percentages
time = df_Q4.groupby("TIME OCC")["count"].count().nlargest(5)  # .sum()
time_perc = round(time / len(df_Q4) * 100, 2).sum()

status_diff = pd.DataFrame(
    {
        "Q4": Q4Status,
        "Q3": Q3Status,
        "DIFF": num_diff,
        "Q4 %": Q4Status_per,
        "Q3 %": Q3Status_per,
        "DIFF %": num_diff_per.round(2),
    }
)

