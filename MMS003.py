import pandas as pd
import numpy as np
from pandas import ExcelWriter

# Get file
file_path = 'prices.xlsx'
margin = 0.43 # CM% by default
df = pd.read_excel(file_path, usecols=['Item no', 'Item name', 'Prod cost'])

# Drop duplicates
df_clean = df.drop_duplicates(subset='Item no', keep ='last')

# Fix cost
df_clean['Prod cost'] = df_clean['Prod cost'].replace(' ', np.nan)
df_clean['Prod cost'] = df_clean['Prod cost'].replace(0, np.nan)
df_clean = df_clean.dropna(subset=['Prod cost'])
df_clean['Prod cost'] = round(df_clean['Prod cost']/(1-margin), 2).astype(np.float32)

# Data type
df_clean['Item name'] = df_clean['Item name'].astype('string')
df_clean['Item no'] = df_clean['Item no'].astype('string')

# Export
df_clean.to_parquet('prices.parquet')
writer = pd.ExcelWriter('clean_prices.xlsx')
df_clean.to_excel(writer, index = False)
writer.save()