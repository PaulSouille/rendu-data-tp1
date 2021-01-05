import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Climat.xlsx', skiprows = 2,  nrows= 32, usecols = 'C:O')
df = df.drop(df.index[0])
df.drop(df.columns[0], axis=1, inplace=True)
df

print(df)