import pandas as pd
from matplotlib import pyplot as plt

# Read the CSV file into a pandas DataFrame
df_karnataka = pd.read_csv('service_msme.csv')

# Generate a bar plot of the data with rotated x-axis labels
ax = df_karnataka.plot.bar(x='district_name', y='total', rot=90)

# Add data labels to the bars using arrows
for i, val in enumerate(df_karnataka['district_name']):
    ax.annotate('{:>s}'.format(val), xy=(i, val), xytext=(0, 5),
                textcoords='offset points', ha='center', va='bottom')

# Set the chart title and axis labels
ax.set_title('Total MSMEs in Karnataka')
ax.set_xlabel('District Name')
ax.set_ylabel('Total MSMEs')

# Display the plot
plt.show()
