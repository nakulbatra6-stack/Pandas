import pandas as pd

# df = pd.read_excel("addleads.xlsx")
# Pandas = Manager
# Excel file = Client speaking French
# openpyxl = Translator

df = pd.read_excel(
    r"C:\Users\nakul\OneDrive\Desktop\Python\Pandas\addleads.xlsx"
)

# print(df)
# print("\nRows:", len(df)) 
# print("Columns:", df.columns.tolist())

print(df.head(),
# df.tail(),
# df.info(),
# df.describe(),
# df.shape,
# df.columns,
# df.dtypes,
# df.loc[df['bd_or_ia'] == 1]
)
# print(df.groupby("leadfrom").count())