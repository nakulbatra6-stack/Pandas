import pandas as pd

df = pd.read_csv("tesla.csv")

print(df.info())
print(df.isnull().sum())


# Date ❌ needs fixing
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek

#sorting by date
df = df.sort_values("Date")

#duplicates
print(df.duplicated().sum())

# If > 0:df.drop_duplicates(inplace=True)

