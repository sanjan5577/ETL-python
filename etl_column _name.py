import requests
import json
import pandas as pd

url = "https://api.data.gov.in/resource/f8cd85a1-f9b8-4ff1-b195-9f75c10eb338?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json"

response = requests.get(url)
json_data = response.json()

# extract the data field from the JSON response
data = json_data["records"]

# convert the data to a DataFrame
df = pd.DataFrame(data)[["_state_name_", "lg_dist_code",
                         "district_name", "micro", "small", "medium", "total"]]

# print the DataFrame
df.to_csv('service_msme.csv', index=False)
