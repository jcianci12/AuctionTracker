
import csv
from bs4 import BeautifulSoup
import requests

url = "https://www.manheim.com.au/damaged-vehicles/auctions/SMS327/page1?franchiseID=SMS"

response = requests.get(url)
with open('page.html', 'w') as f:
    f.write(response.text)
# save the contents to page.html

soup = BeautifulSoup(response.text, 'html.parser')

vehiclecards = soup.find_all('div', class_="vehicle-card")
for vehiclecard in vehiclecards:

    # Extract the useful data using the beatiful soup object
    title = vehiclecard.find('h2', class_='heading vehicle')
    location = vehiclecard.find('span', class_='location')
    odometer = vehiclecard.find('div', class_='odometer')
    colour = vehiclecard.find('div', class_='colour')
    transmission = vehiclecard.find('div', class_='transmission')
    engine = vehiclecard.find('div', class_='engine')
    body = vehiclecard.find('div', class_='bodydesc')
    fuel = vehiclecard.find('div', class_='fuel')
    wovr = vehiclecard.find('div', class_='WOVR')
    stock = vehiclecard.find('div', class_='stock')
    seller = vehiclecard.find('div', class_='seller')

    title = title.text.strip() if title else None
    location = location.text.strip() if location else None
    odometer = odometer.find('div', class_='value').text.strip() if odometer else None
    colour = colour.find('div', class_='value').text.strip() if colour else None
    transmission = transmission.find('div', class_='value').text.strip() if transmission else None
    engine = engine.find('div', class_='value').text.strip() if engine else None
    body = body.find('div', class_='value').text.strip() if body else None
    fuel = fuel.find('div', class_='value').text.strip() if fuel else None
    wovr = wovr.find('div', class_='value').text.strip() if wovr else None
    stock = stock.find('div', class_='value').text.strip() if stock else None
    seller = seller.find('div', class_='value').text.strip() if seller else None

    print(title, location, odometer, colour, transmission, engine, body, fuel, wovr, stock, seller, sep=', ')
    
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, location, odometer, colour, transmission, engine, body, fuel, wovr, stock, seller])
    

    # title = vehiclecard.find('h2', class_='heading vehicle').text.strip()
    # location = vehiclecard.find('span', class_='location').text.strip()
    # odometer = vehiclecard.find('div', class_='odometer').find('div', class_='value').text.strip()
    # colour = vehiclecard.find('div', class_='colour').find('div', class_='value').text.strip()
    # transmission = vehiclecard.find('div', class_='transmission').find('div', class_='value').text.strip()
    # engine = vehiclecard.find('div', class_='engine').find('div', class_='value').text.strip()
    # body = vehiclecard.find('div', class_='bodydesc').find('div', class_='value').text.strip()
    # fuel = vehiclecard.find('div', class_='fuel').find('div', class_='value').text.strip()
    # wovr = vehiclecard.find('div', class_='WOVR').find('div', class_='value').text.strip()
    # stock = vehiclecard.find('div', class_='stock').find('div', class_='value').text.strip()
    # seller = vehiclecard.find('div', class_='seller').find('div', class_='value').text.strip()
    # <div class="card-header">
    #     <div>
    #         <a href="/damaged-vehicles/6969139/2014-iveco-daily-motorhome-gvm-4-495kg?referringPage=SearchResults">
    #             <h2 class="heading vehicle">
    #                 2014 Iveco Daily Motorhome GVM 4,495kg
    #             </h2>
    #         </a>
            

    #         <div class="location-container">
    #             <span class="location">
    #                 <span><i class="icon-facetime-video"></i> Simulcast</span> | <span>Off-site: </span><span>Pinkenba, Queensland</span> | 
    #             </span>
    #         </div>
    #     </div>
    #     <div class="optionMenu">

    #             <a href="/account/login?addWatchList=True&amp;vehicle=000000000006969139%7CNA%7CN" class="js-add-to-watchlist watchlist">
    #                 <span class="watchlist-star hidden-xs"></span>
    #                 <span class="watchlist-star-mobile visible-xs" style="z-index: 9999"></span>
    #             </a>

    #         <div class="btn-group downloadMenu" role="group" aria-label="...">
    #             <div class="btn-group" role="group">
    #                 <button type="button" class="btn btn-default dropdown-toggle " data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    #                     <span class="three-dots"></span>
    #                 </button>
    #                 <ul class="dropdown-menu dropdown-menu-right">
    #                     <li>
    #                         <a class="download-brochure-new" onclick="dataLayer.push({ 'event': 'brochure' });window.open('/damaged-vehicles/brochure/createitemdetail?saleId=TMSAL196&amp;itemId=000000000006969139')" href="#">
    #                             Download Brochure
    #                         </a>
    #                     </li>
    #                     <li>
    #                         <a href="#" rel="modal" data-toggle="modal" class="smButtonLinkActive gtm-emailfriend gtm-socialmedia share-listing-new" onclick="dataLayer.push({ 'event': 'emailfriend' });" data-url="/damaged-vehicles/email/senditemdetails?type=S&amp;itemID=000000000006969139&amp;saleID=TMSAL196">
    #                             Share Listing
    #                         </a>
    #                     </li>
    #                     <li>
    #                             <a href="/products-and-services/transport" target="_blank" class="transport-quote-new">Transport Quote</a>
    #                     </li>
    #                 </ul>
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # <div class="vdp-badges-div">
                                                        
    # </div>
    # <div class="card-content">

    #     <div class="details">
    #         <h3 class="sr-only">Key details</h3>

    #             <div class="odometer col-xs-6">
    #                     <div class="heading hidden-xs">Odometer</div>
    #                     <div class="value">
    #                         112,791 KM Showing
    #                     </div>
    #             </div>

    #             <div class="colour col-xs-6">
    #                 <div class="heading hidden-xs">Colour</div>
    #                 <div class="value">
    #                     White
    #                 </div>
    #             </div>

    #             <div class="transmission col-xs-6">
    #                 <div class="heading hidden-xs">Transmission</div>
    #                 <div class="value">
    #                     AMT
    #                 </div>
    #             </div>

    #             <div class="engine col-xs-6">
    #                 <div class="heading hidden-xs">Engine</div>
    #                 <div class="value">
    #                     4 Cyl, Turbo
    #                 </div>
    #             </div>

    #             <div class="bodydesc col-xs-6">
    #                 <div class="heading hidden-xs">Body</div>
    #                 <div class="value">
    #                     Motorhome
    #                 </div>
    #             </div>

    #             <div class="fuel col-xs-6">
    #                 <div class="heading hidden-xs">Fuel</div>
    #                 <div class="value">
    #                     Diesel
    #                 </div>
    #             </div>

    #             <div class="WOVR col-xs-6">
    #                 <div class="heading hidden-xs">WOVR</div>
    #                 <div class="value">
    #                     No WOVR Record
    #                 </div>
    #             </div>

    #             <div class="stock col-xs-6">
    #                 <div class="heading hidden-xs">Stock No</div>
    #                 <div class="value">
    #                     6969139
    #                 </div>
    #             </div>

    #             <div class="seller col-xs-6">
    #                 <div class="heading hidden-xs">Seller Type</div>
    #                 <div class="value">
    #                     Insurer
    #                 </div>
    #             </div>
            
    #     </div>
    # </div>
    

# print the element


# Print the list of texts
# print(soup)
