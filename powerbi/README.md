# Power BI report build

## Import

1. Open Power BI Desktop.
2. Select **Get data → Text/CSV** and import the repository's `retail_sales.csv`.
3. Rename the query/table to `retail_sales`. Set `Date` to Date, the numeric fields to Whole Number, and `Total Amount` to Decimal Number.
4. Create a calendar table, mark it as the date table, and create a relationship from `Calendar[Date]` to `retail_sales[Date]`.
5. Add the measures from [`measures.dax`](measures.dax). Apply [`retail_theme.json`](retail_theme.json) using **View → Browse for themes**.

## Suggested one-page report

- KPI cards: Total Sales, Transactions, Average Transaction Value, Units Sold.
- Line chart: monthly Total Sales, using Calendar month.
- Clustered bar chart: Total Sales by Product Category.
- Stacked column chart: transactions by Gender and Product Category.
- Slicers: Date, Product Category, Gender.
- Tooltip or detail table: transaction date, category, quantity and total amount.

## Validation checks

With the unfiltered full dataset, the cards should show 456,000 sales, 1,000 transactions, 456.00 average transaction value and 2,514 units sold. The monthly trend includes two transactions on 1 January 2024 (1,530 combined); filter to 2023 when comparing complete months or calculating 2023 growth.

The repository's `images/retail_sales_dashboard.svg` is a static preview of the report layout and data. It is not an exported Power BI Desktop screenshot or a native `.pbix` file. Save the finished report as `powerbi/retail_sales_dashboard.pbix` from Power BI Desktop when available.
