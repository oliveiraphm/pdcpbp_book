import requests
import pandas as pd

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'drinks' in data:

        df = pd.DataFrame(data['drinks'])

        print(df.head())
    else:
        print("No drinks found.")
else:
    print(f"Failed to retrieve data from API. Status code: {response.status_code}")