import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = {
    "Name": ["Amit", "Neha", "Riya", "Raj"],
    "Marks": [75, 85, 60, 90]
}

df = pd.DataFrame(data)

# Bar Plot
sns.barplot(x="Name", y="Marks", data=df)

plt.title("Student Marks")
plt.show()