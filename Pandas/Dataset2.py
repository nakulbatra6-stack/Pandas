import pandas as pd 
df = pd.read_csv("netflix_titles.csv")
# print(df.groupby("type").size())



#PART-1
#How many rows & columns?
# print(df.shape)
# Which columns have missing values?
# print(df.isnull().sum())
#What are data types?
# print(df.info())
# print(df.describe())

#PART-2
# Filter only Movies
# print(df[df["type"] == "Movie"])
#Filter shows released after 2015
# print(df[df["release_year"] > 2015 ])
#Sort by release year descending
# print(df.sort_values(by = "release_year",ascending=False))
# Find all TV Shows from India
# print(df[( df["type"] == "TV Show") & (df["country"] == "India")])

# Find top 10 latest releases
# df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
# print(df['date_added'])
# print(df.sort_values(by="date_added", ascending=False).head(5))

# print(df.sort_values(by = "date_added",ascending=False))

# Count how many Movies vs TV Shows
# print(df.groupby("type").size())
# print(df["type"].value_counts())

# Count missing BEFORE
# missing_before = df["director"].isnull().sum()

# # Fill missing values
# df["director"] = df["director"].fillna("No Director")

# # Count missing AFTER
# missing_after = df["director"].isnull().sum()

# # Print results
# print("Missing before:", missing_before)
# print("Missing after:", missing_after)

# print(df.duplicated().sum())
df.drop_duplicates(subset=["date_added"], inplace=True)#keeps NaN as a value
print(df)
print(df.groupby("date_added"))#EXCLUDES NaN by default
print(df.groupby("date_added", dropna=False).size())
print(df["date_added"].isnull().sum())