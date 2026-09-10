import pandas as pd

df = pd.read_csv("house-price.csv")
# df[df['Address'].isnull()]
df = df.dropna(subset=['Address'])
print(df.isnull().sum())   # باید Address حالا 0 نشون بده
print(len(df))             # تعداد ردیف‌های باقی‌مونده