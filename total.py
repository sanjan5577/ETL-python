import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('service_msme.csv')

# Calculate the sum of values in a single column
column_sum = df['total'].sum()

# Display the sum of values in the column
print(column_sum)
