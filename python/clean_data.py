import pandas as pd

df = pd.read_csv("../data/employees_raw.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Clean text columns
df["Department"] = df["Department"].str.strip()
df["Gender"] = df["Gender"].str.strip()

# Save cleaned data
df.to_csv(
    "../data/employees_clean.csv",
    index=False
)

print("Data Cleaning Completed")