import pandas as pd
from sqlalchemy import create_engine
import time

time.sleep(10)

df = pd.read_csv('/app/data/sales.csv')

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['order_date'] = pd.to_datetime(df['order_date'])
df['total_amount'] = df['quantity'] * df['price']

engine = create_engine('postgresql://aya:aya123@postgres:5432/sales_db')

df.to_sql('sales', engine, if_exists='replace', index=False)

print("ETL Done ✅")
