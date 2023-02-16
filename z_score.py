import pandas as pd
import seaborn as sn

df = pd.read_csv("bhp.csv")
print(sn.histplot(df.price_per_sqft, kde=False))