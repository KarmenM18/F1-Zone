import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the F1 data
url = 'https://www.formula1-dictionary.net/drivers_all_time_list.html'

def scrape_table(url):

    '''
    Sends a GET request to the website
    '''
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first table (or change the table selection if needed)
        table = soup.find('table', {'class': 'excel4'})

        # Extract rows from the table (excluding the header)
        rows = table.find_all('tr')[1:]



