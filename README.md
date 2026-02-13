# retail-sales-analysis

![Retail Analysis Banner](https://via.placeholder.com/800x200?text=Retail+Sales+Insights)  <!-- Optional: Add a banner image via Canva -->

## Overview
This project analyzes a retail sales dataset to uncover trends, category performance, and customer demographics. Built with Python (pandas, matplotlib, seaborn), it demonstrates exploratory data analysis (EDA) skills applied to real-world retail scenarios—drawing from my 14+ years as a Retail Sales Supervisor and AI Training SME (e.g., Power BI dashboards reducing reporting time by 30% at Dubai Duty Free).

Key insights include:
- Monthly sales trends over time.
- Sales distribution by product category.
- Age demographics by gender.

This repo showcases data handling, visualization, and insights generation—transferable to data analyst or retail AI roles.

## Dataset
- Source: [Retail Sales Dataset on Kaggle](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- Columns: Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount.
- Size: ~1000 rows (fictional retail data for privacy).

## Setup
1. Clone the repo: `git clone https://github.com/ayethetthetkhaing/retail-sales-analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python analysis.py` (generates plots in /images).

## Analysis Highlights
- **Monthly Sales Trends**: Line plot showing aggregated sales over time.
  ![Monthly Sales](images/monthly_sales.png)
- **Sales by Category**: Bar chart of total sales per product category.
  ![Category Sales](images/category_sales.png)
- **Age by Gender**: Boxplot of customer age distribution.
  ![Age Gender](images/age_gender.png)

## Code Snippet Example
```python
# From analysis.py - Sales by category
category_sales = df.groupby('Product Category')['Total Amount'].sum()
category_sales.plot(kind='bar')
plt.title('Sales by Product Category')
plt.savefig('images/category_sales.png')
