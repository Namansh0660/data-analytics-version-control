import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
df = df.drop_duplicates()
df.columns = df.columns.str.lower()
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed!")
