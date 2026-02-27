import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")


plt.plot(df["Day"], df["Sales"])
plt.title("Daily Sales Report")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()


plt.bar(df["Day"], df["Sales"])
plt.title("Sales Comparison")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()