import pandas as pd

df = pd.read_csv("tesla.csv")

# print(df.info())
# print(df.isnull().sum())


# Date ❌ needs fixing
# df["Date"] = pd.to_datetime(df["Date"])#default pandas assumes MM-DD-YYYY
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
# print(df.info())

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek

#sorting by date
df = df.sort_values("Date")

#duplicates
# print(df.duplicated().sum())
# If > 0:df.drop_duplicates(inplace=True)

# scaling
num_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

# normalization
for col in num_cols:
    print(col)
    df[col + "_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# standardization
for col in num_cols:
    df[col + "_std"] = (df[col] - df[col].mean()) / df[col].std()

print(df[["Open", "Open_norm", "Open_std"]].head())