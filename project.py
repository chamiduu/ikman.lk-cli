import requests
from bs4 import BeautifulSoup
from PIL import Image
import sys 
import argparse
import os

print('Welcome to Ikman.lk Command Line Interface......')
print('Enter " -h " to for help and info')
print('Enter " exit() " to exit the program')
print('Or just type what you want and hit ENTER key !')
print()

for i in range (1000):
    
    keyword1 = input(' ')

    if keyword1 == '-h':
        print()
        print('This is a CLI (Command line interface) for ikman.lk online craglist site')
        print('Version 0.2')
        print('Developed by Chamindu J. Amarasinghe')
        print('Contact me at chamindujs@gmail.com')
        print('Enter " -h " to for help and info')
        print('Enter " exit() " to exit the program')
        print('Enter " clear() " to clear the screen')

    elif keyword1 == 'exit()':
        sys.exit()

    elif keyword1 == 'clear()': 
        os.system("clear") 

    else:
        url = 'https://ikman.lk/en/ads?by_paying_member=0&sort=relevance&buy_now=0&query=' + keyword1 + '&page=1'

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        item_list = soup.find_all("span", {"class":'title--3yncE'})
        price = soup.find_all("div", {"class":'price--3SnqI color--t0tGX'})
        link = soup.find_all("a", {"class":'card-link--3ssYv gtm-ad-item'})

        links = []

        for link in soup.find_all("a", {"class":'card-link--3ssYv gtm-ad-item'}):
            links.append(link.get('href'))

        count = 0

        final_link = 'https://ikman.lk' + links[count]
        os.system("clear")
        def get_list():
            for i in range (16):
                global count
                print()
                print(item_list[count].text)
                print(price[count].text)
                print(final_link)
                count = count + 1
                print()
    
        get_list() 
         
        print()
        



