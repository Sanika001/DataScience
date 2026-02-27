import pandas as pd


df = pd.read_csv("sales_data.csv")

print("Full Data:")
print(df)

df["Revenue"] = df["Price"] * df["Quantity"]

print("\nWith Revenue Column:")
print(df)


total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)


category_revenue = df.groupby("Category")["Revenue"].sum()
print("\nCategory Wise Revenue:")
print(category_revenue)


most_sold = df.loc[df["Quantity"].idxmax()]
print("\nMost Sold Product:")
print(most_sold)