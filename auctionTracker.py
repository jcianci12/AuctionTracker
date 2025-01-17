import csv
import json
import sqlite3
from bs4 import BeautifulSoup
import requests

def connecttodbandcreateifdoesntexist():
    conn = sqlite3.connect('auctions.db')
    return conn
def addtodb(jsondata):
    # here is a sample of the json data
   #{'title': '2013 Nissan Navara D40 ST Dual Cab Utility', 'location': 'Item Location: Bridgewater, Hobart, Tasmania                                \n|\r\n                                    Lot 1000', 'odometer': '230,174 KM Showing', 'colour': 'Silver', 'transmission': '6spd Manual', 'engine': '4 Cyl, 2.5L, Turbo', 'body': 'Dual Cab Utility', 'fuel': 'Diesel', 'wovr': 'Repairable Write-off', 'stock': '6963313', 'seller': 'Insurer'}
    
    
    conn = connecttodbandcreateifdoesntexist()
    conn.execute("CREATE TABLE IF NOT EXISTS auction (title TEXT, location TEXT, odometer TEXT, colour TEXT, transmission TEXT, engine TEXT, body TEXT, fuel TEXT, wovr TEXT, stock TEXT, seller TEXT, number_of_bids TEXT, bid_status TEXT, current_price TEXT)")
    # insert data into table
    
    conn.executemany("INSERT INTO auction VALUES (:title, :location, :odometer, :colour, :transmission, :engine, :body, :fuel, :wovr, :stock, :seller,:number_of_bids,:bid_status,:current_price)", jsondata)
    # conn.executemany("INSERT INTO auction (title, location, odometer, colour, transmission, engine, body, fuel, wovr, stock, seller) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", jsondata)
    conn.commit()
    conn.close()
    
def scrape_vehicle_data(soup):
    vehicle_data = []
    vehiclecards = soup.find_all('li', class_='vehicle-item')
    for vehiclecard in vehiclecards:
        data = {}
        data['title'] = vehiclecard.find('h2', class_='heading vehicle').text.strip() if vehiclecard.find('h2', class_='heading vehicle') else None
        data['location'] = vehiclecard.find('span', class_='location').text.strip() if vehiclecard.find('span', class_='location') else None
        data['odometer'] = vehiclecard.find('div', class_='odometer').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='odometer') else None
        data['colour'] = vehiclecard.find('div', class_='colour').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='colour') else None
        data['transmission'] = vehiclecard.find('div', class_='transmission').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='transmission') else None
        data['engine'] = vehiclecard.find('div', class_='engine').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='engine') else None
        data['body'] = vehiclecard.find('div', class_='bodydesc').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='bodydesc') else None
        data['fuel'] = vehiclecard.find('div', class_='fuel').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='fuel') else None
        data['wovr'] = vehiclecard.find('div', class_='WOVR').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='WOVR') else None
        data['stock'] = vehiclecard.find('div', class_='stock').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='stock') else None
        data['seller'] = vehiclecard.find('div', class_='seller').find('div', class_='value').text.strip() if vehiclecard.find('div', class_='seller') else None
# we also need to get the number of bids and the current price
#<div class="bidDetials"><span id="nrbids-6963313" class="bids">7</span> <span id="bidtxt-6963313" class="current-status">Current Bid</span> <span id="stprice-6963313" class="price">$1,575</span></div>
        # we also need to get the number of bids and the current price
        data['number_of_bids'] = None
        data['bid_status'] = None
        data['current_price'] = None
        if vehiclecard:
            bid_span = vehiclecard.find('span', class_='bids')
            if bid_span:
                data['number_of_bids'] = bid_span.text.strip()
            bid_status = vehiclecard.find('span', class_='current-status')
            if bid_status:
                data['bid_status'] = bid_status.text.strip()
            price_span = vehiclecard.find('span', class_='price')
            if price_span:
                data['current_price'] = price_span.text.strip()

        vehicle_data.append(data)

    return vehicle_data

#get a list of pages that dont return a 404
def getPageList(url):
    #
    #using beatiful soup, extract the count of pages
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find_all('li', class_='borderlist')
    return len(a)

def replacepageinurl(url,index):
    return url.replace("page"+str(index), "page"+str(index+1))
def fetchurlandreturnsoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

connecttodbandcreateifdoesntexist()


json_master_list = {}
# Example usage:
url_to_scrape = "https://www.manheim.com.au/damaged-vehicles/auctions/SMS327/page1?franchiseID=SMS"
pagelength = getPageList(url_to_scrape)
#for i in pagelenth 
#example page length = 16
for i in range(0,pagelength):

    newurl = replacepageinurl(url_to_scrape,i)
    soup = fetchurlandreturnsoup(newurl)
    json_data = scrape_vehicle_data(soup)

    addtodb(json_data)


print("Done")
