import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = 'https://www.formula1-dictionary.net/drivers_all_time_list.html'
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find the first table with class "excel4" and extract headers + data
table = soup.find('table', {'class': 'excel4'})

# Extract headers from the first class
headers = [td.text.strip() for td in table.find_all('tr')[0].find_all('td')]

# Extract first table data (skip the header)
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:  # Only append if there are columns
        data.append([col.text.strip() for col in cols])

# Step 4: Find all <tr> elements for other classes and append data
# Note: We'll include a simple method to get rows from the other classes
# This loop will get all rows and check for other class types if needed
other_classes = ['excel113', 'excel119', 'excel24', 'excel29']

# Loop through all classes and check if class name is in the row
for class_name in other_classes:
    # Find the next table or section that contains rows of interest
    additional_tables = soup.find_all('table', {'class': class_name})

    for additional_table in additional_tables:
        for row in additional_table.find_all('tr'):
            cols = row.find_all('td')
            if cols:  # Only append non-empty rows
                data.append([col.text.strip() for col in cols])

# Step 5: Convert data to a DataFrame and save as CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv('formula1_drivers_all_time.csv', index=False)
