import json

# Read the JSON data from the local file
with open('data.json') as f:
    data = json.load(f)

# Initialize an empty dictionary to store the results
result = {}

# Loop over each city in the data
for city_data in data:
    city = city_data['city']
    products = city_data['products']
    
    # Sort the products by price in descending order
    sorted_products = sorted(products, key=lambda x:x['price'], reverse=True)
    
    # Take the top 3 most expensive products and store them in the result dictionary
    result[city] = [(p['name'], p['price']) for p in sorted_products[:3]]

# Print the result dictionary
print(result)
