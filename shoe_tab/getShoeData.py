from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import gmtime


shoe_brand = {
    'Nike': 'nike-release-dates',
    "Air Jordan": 'air-jordan-release-dates',
    "Adidas": 'adidas-release-dates'
}

def retrieveData(brand):
    data = {}
    data['releases'] = []

    year = gmtime().tm_year
    month = gmtime().tm_mon
    yearChange = False

    for months in range(month,month+3):
        #if z > 12 then that means the year must change
        if(months > 12):
            if(not yearChange):
                year += 1
                yearChange = True
            months = months%12
        
        #formats month value
        monthVal = ""
        if(months    < 10):
            monthVal = f"0{months}"
        else:
            monthVal = f"{months}"

        print(f'https://solecollector.com/sneaker-release-dates/{shoe_brand[brand]}/{year}/{monthVal}/')
        #requests the url
        response = requests.get(f'https://solecollector.com/sneaker-release-dates/{shoe_brand[brand]}/{year}/{monthVal}/')
        soup = BeautifulSoup(response.content, 'html.parser')

        #gets all the images and shoe data
        releases = soup.find_all('div', class_= "add-to-calendar")
        release_images = soup.find_all('div', class_='sneaker-release__img-16x9')
        release_prices = soup.find_all('span', class_='sneaker-release__option')

        #traverses the response and gets adds the name,data and image to a dictionary


        for x in range(len(releases)):

            shoe_name = releases[x]['data-release-name']
            if('/' in shoe_name):
                shoe_name = shoe_name[0 : shoe_name.find("/")][0:  shoe_name.rfind(" ")]
                

            data['releases'].append({
                "Shoe_Name": shoe_name,
                'Release_Date': releases[x]['data-date'][:releases[x]['data-date'].rfind(' ')],
                'Release_Time':  releases[x]['data-date'][releases[x]['data-date'].rfind(' '):],
                "Image": str(release_images[x].find_all('img', src = True)[0]['src']),
                "Price": release_prices[x].text

            })
            
    return data['releases']