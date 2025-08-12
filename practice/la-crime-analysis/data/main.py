import pandas as pd

df = pd.read_csv("data/raw/Crime_Data_from_2020_to_Present.csv")
df.columns
df["count"] = 1


r_vt = df.loc[
    (df["Crm Cd Desc"].str.contains("VEHICLE - STOLEN"))
    & (df["AREA NAME"].str.contains("Rampart", regex=True))
]

r_vt_df = pd.DataFrame()

r_vt_df = r_vt.reset_index(drop=True)
r_vt_df["count"].count()

cols = list(r_vt_df.columns)

r_vt_df = r_vt[["DATE OCC", "Crm Cd Desc", "AREA NAME", "Status Desc", "TIME OCC"]]

r_vt_df["quarter"] = pd.to_datetime(r_vt_df["DATE OCC"]).dt.to_period("Q")

r_vt_df["quarter"].dt.year.unique()

r_vt_df.to_csv("data/procesed/RampartVehicleThefts.csv", index=False)
