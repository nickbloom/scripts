from urllib import request
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
rows = []

# OBAMA
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=44&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])

# GW BUSH	
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=43&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])

# CLINTON
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=42&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])


with open('/Users/nbloom/Desktop/clinton.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(row for row in rows if row)

# GHW BUSH
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=41&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])


with open('/Users/nbloom/Desktop/clinton.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(row for row in rows if row)	

# Reagan
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=40&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])

# Carter
url='http://www.presidency.ucsb.edu/data/popularity.php?pres=39&sort=time&direct=DESC&Submit=DISPLAY'

html = request.urlopen(url).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)

table=soup.find("table", width=600)
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr'):
	rows.append([val.get_text() for val in row.find_all('td')])



with open('/Users/nbloom/Desktop/prez.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(row for row in rows if row)	


http://stackoverflow.com/questions/14167352/beautifulsoup-html-csv