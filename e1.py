import requests
from bs4 import BeautifulSoup as bs

url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(url)
html = resp.content
soup = bs(html , "html.parser")
IDs = soup.find_all("tr", "election_item")

with open("ELECTION_ID", "w") as out:
    for row in IDs:
        year = row.find("td", "year first").string
        ID_number = row.get("id").replace("election-id-", "")
        out.write("{} {}\n".format(year, ID_number))
# generate two new variables, and print this two variables to the file "ELECTION-ID"
