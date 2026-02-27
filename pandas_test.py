import pandas as pd

print(pd.__version__)

data = {"Name": ["Amit", "Neha"], "Salary": [50000, 60000]}
df = pd.DataFrame(data)

print(df)