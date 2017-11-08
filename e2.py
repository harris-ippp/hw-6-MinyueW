import requests
from bs4 import BeautifulSoup as bs

url_t = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID"):
    lines = line.split()
    line1=lines[1]
    line2=lines[0]
    url = url_t.format(line1)
    resp = requests.get(url)
    for i in line2:
        fname = "president_general_" + line2 +".csv"
        with open(fname, "w") as out:
            out.write(resp.text)
# split each line
# create files and write data for each election to each file
