import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("students.csv")

print("Full Data:")
print(df)


df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("\nWith Average:")
print(df)


topper = df.loc[df["Average"].idxmax()]
print("\nTopper:")
print(topper)


sns.barplot(x="Name", y="Average", data=df)
plt.title("Student Average Marks")
plt.show()