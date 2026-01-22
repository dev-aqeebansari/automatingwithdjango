from bs4 import BeautifulSoup
import requests

# url = "https://webscraper.io/test-sites/tables"

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
headers = {
    "User-Agent": "PythonistWikiScraper/1.0 (contact: extctopper06@gmail.com)"
}
response = requests.get(url, headers=headers)
# print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')

datatype_table = soup.find(class_="wikitable")
# print(datatype_table)
body = datatype_table.find('tbody')
rows = body.find_all('tr')[1:]

mutable_types = []
immutable_types = []

for row in rows:
    data = row.find_all('td')
    if data[1].get_text() == 'mutable\n':
        mutable_types.append(data[0].get_text().strip())
    else:
        immutable_types.append(data[0].get_text().strip())

print(f"Mutable types: {mutable_types}")
print(f"Immutable types: {immutable_types}")








# # print(soup)
# headings1 = soup.find_all('h1')
# headings2 = soup.find_all('h2')
# # print(headings1)
# # print(headings2)
# images = soup.find_all('img')
# # print(images)
# # print(images[0]['src'])
# tables = soup.find_all('table')[0]
# rows =  tables.find_all('tr')[1:]

# last_names = []
# for row in rows:
#     last_names.append(row.find_all('td')[2].getText())
#     # last_names.append

# print(last_names)