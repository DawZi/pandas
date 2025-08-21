# Pizzeria data analysis

## Overview
This project analyzes sales and order data from a pizzeria. It includes data processing and visualization scripts to explore pizza sales trends, order patterns, and category performance. Visualizations, such as bar charts for total sales by category, best-selling pizzas, and worst-selling pizzas

## Dataset
- **Location:** `projects/pizzeria-data-analysis/data/raw/pizza_sales.csv`
- **Size:** 48620 rows × 12 columns

## Processed Data
- `data/formated/day_sales.csv` – Sales by day of the week 
- `data/formated/orders_by_hour.csv` – Orders grouped by hour  
- `data/formated/sale_numbers.csv` –  Sale numbers by pizza name
- `data/formated/sales_by_category.csv` – Sales per pizza category 
- `data/formated/sales_by_size.csv` – Sales by pizza size

## Insights
- Sales peak on Fridays (8106) and are lowest on Sundays (5917), showing strong end-of-week demand. 
- Orders surge at lunch (12h) and dinner (18h), with little demand outside meal times.
- Sales by pizza size: Large pizzas (38.1%) are the most popular, while XL and larger sizes (1.18%) barely sell
- Classic pizzas lead sales at nearly 30%, while the other three categories are evenly distributed around 22-24%.

## Visualizations
- ![General numbers](plots/general_numbers.png)
- ![Sales by day](plots/pizza_sales_by_day.png)
- ![Orders per given hour](plots/order_count_by_hour.png)
- ![Sales by pizza size pie chart](plots/sales_by_size_pie.png)
- ![Sales by pizza category pie chart](plots/sales_by_category_pie.png)
- ![Total sales by pizza category](plots/total_sales_by_category.png)
- ![Five best selling pizzas](plots/best_selling_pizza.png)
- ![Five worst selling pizzas](plots/worst_seling_pizza.png)
