# US Births analysis

## Overview
This project analyzes data from [Data](https://github.com/fivethirtyeight/data/tree/4c1ff5e3aef1816ae04af63218015066e186c147) repository.  
It includes both data processing and visualization scripts.

## Dataset
- **Source:** [FiveThirtyEight data](https://github.com/fivethirtyeight/data/tree/4c1ff5e3aef1816ae04af63218015066e186c147)
- **Location:** `projects/us-births-analysis/data/raw/US_births_2000-2014_SSA.csv`
- **Size:** 5,479 rows × 5 columns

## Processed Data
- `projects/us-births-analysis/data/formated/births_by_date.csv` – Birth counts grouped by exact date  
- `projects/us-births-analysis/data/formated/births_by_day.csv` – Birth counts grouped by day of the week  
- `projects/us-births-analysis/data/formated/births_by_month.csv` – Birth counts grouped by month  
- `projects/us-births-analysis/data/formated/highest_births_by_date.csv` – Dates with the highest recorded birth counts  
- `projects/us-births-analysis/data/formated/lowest_births_by_date.csv` – Dates with the lowest recorded birth counts  

## Visualizations 
- ![Average births per month](plots/average_per_month.png)  
- ![Birth counts per year](plots/births_per_year.png)  
- ![Day with least births](plots/least_births_day.png)  
- ![Day with most births](plots/most_births_day.png)  
- ![Birth volumes across the week](plots/week_volumes.png)  
- ![Birth volumes across the week (pie chart)](plots/week_volumes_pie.png)  
