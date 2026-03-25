import pandas as pd

data = {
    "name": ["Nakul", "Aman", "Riya"],
    "age": [24, 26, 23]
}

df = pd.DataFrame(data)

# df.set_index("name", inplace=True) #dont want to see index

df.index = ['a', 'b', 'c'] #Create your own index
print(df)