from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import gmtime

# Shoe brands link headers
shoe_brand = {
    'Nike': 'nike-release-dates',
    "Air Jordan": 'air-jordan-release-dates',
    "Adidas": 'adidas-release-dates'
}

# Note: This list needs to be added to
hypeList = ['OffWhite', 'Bred', 'Dior', 'Royal', ' x ', ' X ', 'Off', ' off ']


def retrieveData(brand):
    """Retrieves the shoe data for shoe by brand"""

    data = {}
    data['releases'] = []
    data['hyped'] = []

    year = gmtime().tm_year
    month = gmtime().tm_mon
    yearChange = False

    for months in range(month, month+3):
        # if z > 12 then thar means the year must change
        if(months > 12):
            if(not yearChange):
                year += 1
                yearChange = True
            months = months % 12
        # formats month value
        monthVal = ""
        if(months < 10):
            monthVal = f"0{months}"
        else:
            monthVal = f"{months}"

        # requests the url
        response = requests.get(f'https://solecollector.com/sneaker-release-dates/{shoe_brand[brand]}/{year}/{monthVal}/')
        soup = BeautifulSoup(response.content, 'html.parser')

        # gets all the images and shoe data
        releases = soup.find_all('div', class_="add-to-calendar")
        release_images = soup.find_all('div', class_='sneaker-release__img-16x9')
        release_prices = soup.find_all('span', class_='sneaker-release__option')

        # traverses the response and gets adds the name,data and image to a dictionary
        for x in range(len(releases)):
            # Removes color styles from shoe name
            shoe_name = releases[x]['data-release-name']
            if('/' in shoe_name):
                shoe_name = shoe_name[0 : shoe_name.find("/")][0:shoe_name.rfind(" ")]
            # Appends the data to a dictionary list
            data['releases'].append({
                "Shoe_Name": shoe_name,
                'Release_Date': releases[x]['data-date'][:releases[x]['data-date'].rfind(' ')],
                'Release_Time': releases[x]['data-date'][releases[x]['data-date'].rfind(' '):],
                "Image": str(release_images[x].find_all('img', src=True)[0]['src']),
                "Price": release_prices[x].text
            })
            if isHyped(shoe_name):
                data['hyped'].append({
                    "Shoe_Name": shoe_name,
                    'Release_Date': releases[x]['data-date'][:releases[x]['data-date'].rfind(' ')],
                    'Release_Time': releases[x]['data-date'][releases[x]['data-date'].rfind(' '):],
                    "Image": str(release_images[x].find_all('img', src=True)[0]['src']),
                    "Price": release_prices[x].text
                })

    # Returns the data back to views.py
    return data['releases'], data['hyped'] 


def isHyped(shoe_name):
    for hyped in hypeList:
        if hyped in shoe_name:
            return True
    return False
