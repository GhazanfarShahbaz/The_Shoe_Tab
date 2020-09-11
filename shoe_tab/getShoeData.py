import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import gmtime
from .models import Shoe


# Shoe brands link headers
shoe_brand = {
    'Nike': 'nike-release-dates',
    "Air Jordan": 'air-jordan-release-dates',
    "Adidas": 'adidas-release-dates'
}

# Note: This list needs to be added to
hypeList = ['OffWhite', 'Bred', 'Dior', 'Royal', ' x ', ' X ', 'Off', ' off ', 'Toe']

def allData():
    return Shoe.objects.filter(hyped = True)

def gate(brand):
    """Used to see wether or not the calender data needs updating or not"""
    if gmtime().tm_mday == 1:
        retrieveData(brand)

    year = gmtime().tm_year
    month = gmtime().tm_mon
    day = gmtime().tm_mday
    return Shoe.objects.filter(shoe_brand=brand,hyped=False, release_day__gte=day, release_month__gte= month, release_year__gte=year ), Shoe.objects.filter(shoe_brand=brand, hyped = True, release_day__gte=day, release_month__gte= month, release_year__gte=year )

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

            date = releases[x]['data-date'][:releases[x]['data-date'].rfind(' ')].split('/')

            new_shoe = Shoe()
            new_shoe.shoe_name = shoe_name
            new_shoe.shoe_brand = brand
            new_shoe.release_day = int(date[1])
            new_shoe.release_month = int(date[0])
            new_shoe.release_year = int("20" + str(date[2]))
            new_shoe.release_time = releases[x]['data-date'][releases[x]['data-date'].rfind(' '):]
            new_shoe.image = str(release_images[x].find_all('img', src=True)[0]['src'])
            new_shoe.price = release_prices[x].text
            new_shoe.hyped = isHyped(shoe_name)

            if new_shoe not in Shoe.objects.all():
                new_shoe.save()

def isHyped(shoe_name):
    """Checked if shoe is hyped or not"""
    for hyped in hypeList:
        if hyped in shoe_name:
            return True
    return False
