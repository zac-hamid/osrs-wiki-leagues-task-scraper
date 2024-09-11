import requests
import sys
from bs4 import BeautifulSoup
import csv
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-l", "--league", choices = ['TBR', 'RE'], default = "RE", help = "The league to scrape task list for. TBR = Trailblazer Reloaded, RE = Raging Echoes")
parser.add_argument("-o", "--output", default = "tasks", help = "The name of the output file (default = tasks)")
args = parser.parse_args()
print(args.league, args.output);

url_map = {'TBR': 'Trailblazer_Reloaded_League/Tasks', 'RE': 'Raging_Echoes_League/Tasks', }

# URL of the wiki page
url = 'https://oldschool.runescape.wiki/w/' + url_map[args.league]

# Fetch the webpage
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tables on the page
tables = soup.find_all('table')

# Target table with specific headers

target_headers_map = {'TBR': ["Area", "Name", "Task", "Requirements", "Pts", "Comp%"], 'RE': ["Area", "Name", "Task", "Requirements", "Pts", "Comp%"]}
target_headers = target_headers_map[args.league]
target_table = None

for table in tables:
    headers = [header.text.strip() for header in table.find_all('th')]
    if all(item in headers for item in target_headers):
        target_table = table
        break

# Check if the target table is found
if target_table is None:
    print("Target table not found.")
    exit()

# Prepare to write to CSV
data = [target_headers]

# Extract table rows and area value
for row in target_table.find_all('tr'):
    # Extracting the area value from the data-tbz-area-for-filtering attribute
    area_value = row.get('data-tbz-area-for-filtering', '').capitalize()
    
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if cols:  # if the row contains data
        cols[0] = area_value  # Replace the first column with the new "Area" value
        data.append(cols)

# Filename for the CSV file
csv_file_name = args.output + '.csv'

# Write data to CSV
with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data written to {csv_file_name}")
