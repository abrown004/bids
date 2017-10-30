from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv

# Extract html page
html = urlopen("http://sv08data.dot.ca.gov/contractcost/results.php?item=12%22+Reinforced+Concrete+Pipe&ob=0&min=&max=&minU=&maxU=&unit=none&start=Search")
html_soup = BeautifulSoup(html, 'html.parser')
#print(html_soup)

###############################################################################
def get_all_bids(html_soup):
    bid = []
    all_rows_in_html_page = html_soup.findAll("tr")
    for table_row in all_rows_in_html_page:
        row_cells = table_row.findAll("td")
        if len(row_cells) == 13:
            bid_entry = {
#                "id": row_cells[0].text,
                "item": row_cells[1].text,
                "unit": row_cells[2].text,
                "quantity": row_cells[4].text,
                "price": row_cells[5].text,
                "date": row_cells[8].text
            }
            bid.append(bid_entry)
    return bid
###############################################################################

print(get_all_bids(html_soup))

# Write JSON file to file
#with open('caltrans.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
#    for line in get_all_bid(html_soup):
#        writer.writerow(line)
