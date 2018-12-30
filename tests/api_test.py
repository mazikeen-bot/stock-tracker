from iexfinance import get_historical_data
from datetime import datetime

start = datetime(2017, 2, 9)
end = datetime(2017, 5, 24)

df = get_historical_data("TSLA", start=start, end=end, output_format='pandas')

df.to_csv("sample_data_tsla.csv")
print(df.tail())