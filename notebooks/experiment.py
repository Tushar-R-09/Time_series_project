import pandas as pd
from src.paths import TRANSFORMED_DATA_DIR
from datetime import datetime
from src.data_split import train_test_split

df = pd.read_parquet(TRANSFORMED_DATA_DIR / 'tabular_data.parquet')

X_train, y_train, X_test, y_test = train_test_split(df, cutoff_date =  datetime(2022, 6, 1, 0, 0, 0), target_column_name='target_rides_next_hour')

print(f'{X_train.shape = }')
print(f'{y_train.shape = }')
print(f'{X_test.shape = }')
print(f'{y_test.shape = }')
