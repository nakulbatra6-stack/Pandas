import pandas as pd

data = [10,20,30]
# s = pd.Series(data)
# print(s)

data = {
    "Name": ["A","B","C"],
    "Age": [21,23,23]
}

df = pd.DataFrame(data)

# print(df["Age"])
# print(df)
# print(df[["Name","Age"]]) #same as print(df)

#used to access rows/columns of a DataFrame.
# print(df.loc[0]) uses label
# print(df.iloc[0]) uses index

# print(df.loc[2, "Name"]) # same as print(df.iloc[2,0])
# print(df.iloc[2,1])

# print(df[df["Age"] > 21])


df["Salary"] = [50000,60000,70000]
# df["Age"] = df["Age"].apply(lambda x: x+1) # increase age by 1 

# print(df.sort_values("Age"))#creates a sorted copy
# print(df)

# print(df.groupby("Age")["Salary"].mean()) 
#works in case of same age's exist
# Age
# 21    55000.0
# 23    70000.0

df.groupby("Age")["Salary"].sum()
df.groupby("Age")["Salary"].max()
df.groupby("AGe")["Salary"].min()
#median,std,var