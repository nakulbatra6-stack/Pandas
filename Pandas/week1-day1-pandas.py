import pandas as pd

# df = pd.read_csv("data.csv")

df = pd.read_excel("data.xlsx")

# print(df.head())#top 5 records
# print(df.tail())#bottom 5 records

# print(df.shape)#(250, 10) rows x columns
# print(df.columns)
# print(df.info())

# print(df['Opened'].value_counts())
# Opened
# Yes    84
# Name: count, dtype: int64

# print(df[df["Opened"] == "Yes"])
#This creates a boolean mask (True/False):
# df["Clicked"] == "Yes"

# 0     True
# 1     False
# 2     True
# 3     False

# df[true] and df[false]
# only print true values 

# print(df[(df["Opened"] == "Yes") & (df["Clicked"] == "Yes")])
#selecting Data 
print(df["Opened"])
print(df[["Recipient","Opened"]]) #df[LIST OF COLUMNS]
print(df[df["Opened"] == "Yes"])
