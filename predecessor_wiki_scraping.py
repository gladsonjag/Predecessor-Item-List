from bs4 import BeautifulSoup
import requests
import pandas
import csv
import json
import re

#working finally holy fuck!
def get_item_data(url):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

    item_data1 = []
    for item in soup.find('div', class_='pi-item pi-data pi-item-spacing pi-border-color').parent.find_all('div'):
        item_data1.append(item.text)
    
    if len(item_data1) > 1:
        item_data1.remove(item_data1[0])
    if len(item_data1) > 2:
        item_data1.remove(item_data1[1])
    if len(item_data1) > 3:
        item_data1.remove(item_data1[2])
    if len(item_data1) > 4:
        item_data1.remove(item_data1[3])
    if len(item_data1) > 5:
        item_data1.remove(item_data1[4])

#26 is the codex item

    item = soup.find_all('td', class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing")
    if len(item) == 3:
        item = item[1]
        if item:
            item = re.sub(r'[^0-9]', '', item.text)
            item = 'Gold ' + item
            item_data1.append(item)
    elif len(item) == 2:
        item = item[0]
        if item:
            item = re.sub(r'[^0-9]', '', item.text)
            item = 'Gold ' + item
            item_data1.append(item)
        
    else:
        item_data1.append('Gold 0')

    #print(item_data1)
    
    
    

    return(item_data1)

def create_url_list(item_name_list):

    url_list = []

    for item_name in item_name_list:
        url_list.append("https://predecessor.fandom.com/wiki/" + str(item_name))

    return(url_list)

#initializing all necessary list
item_name_list = []
urls = []
item_stats = []

#initializing the final product being the item dictionary
items = {}

#opens the item name csv file to be used for url creation and stat labeling
with open('predecessor_item_name.csv', 'r') as read_ob:
    reader = csv.reader(read_ob, delimiter=',')
    for row in reader:
        for name in row:
            item_name_list.append(name)

#creates url list
urls = create_url_list(item_name_list)

#creats the item attribute list. Note each index is corresponding to the index of the item in the item name list
for url in urls:

    item_stats.append(get_item_data(url))

#creates a dictionary to hold the item name and stats in one list
'''
for key in item_name_list:
    for stats in item_stats:
        items[key] = stats
        item_stats.remove(stats)
        break
#test line of code to print the dictonary holding all info
#print(items)
'''

#writes the item_stats list to a .txt file
with open('predecessor_item_stats.csv', 'w') as f:
    for item_stat in item_stats:
        f.write(",".join(item_stat) + "\n")
    f.close()





