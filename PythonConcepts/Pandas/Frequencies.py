import pandas as pd
import numpy as np

# Write a Pandas program to display most frequent value in a given series and replace everything else as ‘Other’ in the series.
num_series = pd.Series(np.random.randint(1, 5, [15]))
# print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
print(num_series.value_counts().index[:1]);
result = num_series[~num_series.isin(num_series.value_counts().index[:0])] = 'Other'
print(num_series)