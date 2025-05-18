import pandas as pd


df = pd.DataFrame({
    'A':['1','2','3'],
    'B':['4.1','5.2','6.3']
})

df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)

print(df.dtypes)