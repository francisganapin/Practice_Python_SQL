import pandas as pd

df = pd.DataFrame({'price':[100,250,80]})
df['label'] = df['price'].apply(lambda x: "Expensive" if x > 200 else "Cheap")


print(df)