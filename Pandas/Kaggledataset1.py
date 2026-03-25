import pandas as pd


df = pd.read_csv("StudentsPerformance.csv")

# print(df.head())

# Filter: students with score > 80
# print(df[df["math score"] > 80])

# print(df.groupby("gender")["math score"].mean())
# print(df.groupby("gender")[["math score","reading score"]].mean())


#Gives total rows per group
# print(df.groupby("gender").count())
# print(df.groupby("gender").size())

# print(df.groupby(["gender","race/ethnicity"]).count())
# print(df.groupby(["gender","race/ethnicity"]).mean())

# print(df.groupby("gender")["math score"].agg(["mean", "min", "max"]))

# 1. Avg writing score by gender
# print(df.groupby("gender")["writing score"].mean())
# 2. Count students by race
# print(df.groupby("race/ethnicity").size())

# 3. Avg all scores by parental education
# print(df.groupby("parental level of education")[["math score","reading score","writing score"]].mean())

df["total score"] = df[["math score", "reading score", "writing score"]].sum(axis=1)#row-wise
print(df.head())