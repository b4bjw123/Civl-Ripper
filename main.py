import sys, csv, requests 
from bs4 import BeautifulSoup

page = requests.get("https://civlcomps.org/event/pga-worlds-2023/participants?ParticipantSearch%5Bgroup%5D=&ParticipantSearch%5Bgroup%5D=gender&ParticipantSearch%5Bstatus%5D=")
soup = BeautifulSoup(page.content, 'html.parser')
pilotJson = []
table = soup.table
rows = table.find_all("tr")
rows.pop(0)
for row in rows:
    if (row.find(attrs={"data-col":"status"}).get("data-value")!="cancelled"):
        country = row.find(attrs={"data-col":"ioc"}).get("data-value")
        pilotJson.append([country,"M"])

table.decompose()
table = soup.table
rows = table.find_all("tr")
rows.pop(0)
for row in rows:
    if (row.find(attrs={"data-col":"status"}).get("data-value")!="cancelled"):
        country = row.find(attrs={"data-col":"ioc"}).get("data-value")
        pilotJson.append([country,"F"])

with open('registered pilots.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(pilotJson)


     

page = requests.get("https://civlcomps.org/ranking/paragliding-accuracy/nations")
soup = BeautifulSoup(page.content, 'html.parser')
nations = []
rows = soup.select(".cms__table__row")
for i, row in enumerate(rows):
    # country = row.select(".col-2")[1].text
    country = row.find_all("div", {"class": "col-2"})[1].text.strip()
    nations.append([i+1, country])
# print(nations)

with open('countries.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(nations)
