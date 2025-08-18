import pandas as pd

df = pd.read_csv("../data/formated/pizza_sales.csv")


# Pizza sales by day
day_sales = df.drop_duplicates(subset="order_id")
day_sales = df["order_date"]
day_sales = pd.to_datetime(day_sales, dayfirst=True).dt.day_name()
day_sales = pd.DataFrame(day_sales.value_counts())
week_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
day_sales = day_sales.reindex(week_order).to_csv("../data/formated/day_sales.csv")

# Hourly trend for total orders
df["order_time"] = pd.to_datetime(df["order_time"], format="%H:%M:%S").dt.hour
orders_by_hour = (
    df.drop_duplicates(subset=["order_id"])
    .groupby("order_time")["order_id"]
    .count()
    .reindex(range(24), fill_value=0)
    .reset_index()
    .to_csv("../data/formated/orders_by_hour.csv", index=False)
)

# sales by pizza size
sales_by_size = pd.DataFrame(df.groupby("pizza_size")["quantity"].count()).reset_index()
sales_by_size["pizza_size"] = sales_by_size["pizza_size"].replace(
    ["XL", "XXL"], "Other"
)
sales_by_size = (
    pd.DataFrame(
        sales_by_size.groupby("pizza_size")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )
    .reset_index()
    .to_csv("../data/formated/sales_by_size.csv", index=False)
)
sales_by_size

# Sales by pizza category in % will do autopct

# Total pizzas sold by category
sales_by_category = (
    pd.DataFrame(
        df.groupby("pizza_category")["quantity"].count().sort_values(ascending=False)
    )
    .reset_index()
    .to_csv("../data/formated/sales_by_category.csv", index=False)
)

# Top 5 best sellers by total pizzas sold
# Top 5 worst sellers by total pizzas sold
sale_numbers = pd.DataFrame(
    df.groupby("pizza_name")["quantity"].count().sort_values(ascending=False)
).to_csv("../data/formated/sale_numbers.csv")
