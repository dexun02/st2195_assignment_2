import os
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Comma-separated_values"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
csv_example = soup.find('pre').text
folder_name = "python_csv"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
csv_file_path = os.path.join(folder_name, 'cars_data.csv')
with open(csv_file_path, 'w') as file:
    file.write(csv_example)
print(f"CSV data saved to '{csv_file_path}'")