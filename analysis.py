import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "images"
OUTPUT.mkdir(exist_ok=True)

# Use the dataset committed at the repository root.
df = pd.read_csv(ROOT / "retail_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Basic EDA
print(df.head())
print(df.describe(include="all"))
print(df.info())

# Monthly sales trend. Keep all dates in the source, including the two
# transactions on 2024-01-01; interpret January 2024 as a partial month.
monthly_sales = (
    df.set_index("Date")["Total Amount"]
      .resample("ME")
      .sum()
)
fig, ax = plt.subplots(figsize=(10, 5))
monthly_sales.plot(ax=ax, marker="o")
ax.set_title("Monthly Sales Trends")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (dataset units)")
fig.tight_layout()
fig.savefig(OUTPUT / "monthly_sales.png", dpi=160)
plt.close(fig)

# Sales by category
category_sales = df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 4))
category_sales.plot(kind="bar", ax=ax)
ax.set_title("Sales by Product Category")
ax.set_xlabel("Product category")
ax.set_ylabel("Sales (dataset units)")
fig.tight_layout()
fig.savefig(OUTPUT / "category_sales.png", dpi=160)
plt.close(fig)

# Customer demographics
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x="Gender", y="Age", data=df, ax=ax)
ax.set_title("Age Distribution by Gender")
fig.tight_layout()
fig.savefig(OUTPUT / "age_gender.png", dpi=160)
plt.close(fig)

print(f"Analysis complete. Plots saved in {OUTPUT}.")
