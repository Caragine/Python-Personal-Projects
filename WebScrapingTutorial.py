# This is a Web Scraping Project tutorial from Alex the Analyst's Data Analyst Bootcamp

from bs4 import BeautifulSoup
import requests

# Import BeautifulSoup and Requests, save URL, page and soup as variables.
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

# Get the elements from table
soup.find_all('table')[1]
table = soup.find_all('table')[1]

#Store the table headers in a variable called world_titles using table.find_all(‘th’)
world_titles = table.find_all('th')

# Strip each world table title with .text and .strip() to clean it
world_table_titles = [title.text.strip() for title in world_titles]

# Use pandas to create the DataFrame with the header titles
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

# For each row in column_data, create row_data and strip data to store it
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

# Use df length in order to place each new row of data in the next row of df
    length = len(df)
    df.loc[length] = individual_row_data

# By default it will have an index column, index=False will fix that so that rank column isnt put twice
df.to_csv(r'D:/Python Personal Projects/Python-Personal-Projects/CompanyRevenueFromWiki.csv', index=False)