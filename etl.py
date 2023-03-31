import requests
import csv
import pandas as pd


base_url = 'https://api.data.gov.in/resource/f8cd85a1-f9b8-4ff1-b195-9f75c10eb338?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit=1000'


r = requests.get(base_url)

data = r.json()

records = data['records']

df = pd.DataFrame(records)

df = df.drop('last_updated', axis=1)

df.to_csv('first10.csv', index=False)
