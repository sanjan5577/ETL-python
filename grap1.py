import pandas as pd
from matplotlib import pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('service_msme.csv')

# Generate a bar chart of the data
ax = df.plot.bar(x='district_name', y='total', rot=90)

# Set the title and axis labels
ax.set_title('Total MSMEs in Karnataka')
ax.set_xlabel('DISTRICT_NAME')
ax.set_ylabel('Total MSMEs')

# Save the chart as an image file
plt.savefig('bar_chart.png')
