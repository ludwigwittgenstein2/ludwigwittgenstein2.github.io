#Author: Rick Rejeleene
#Date: Sep 5, 2018
#Midnight-Sleepy
#Github-Reading
#key:sBITGRylosZkjIAaixQ
#secret:1NAektAdA5vKqlzC1ciJIOF8JyKSPtjKI9xUxipExY
#Version:0.1
#https://www.goodreads.com/api/index


import requests

response = requests.get('https://www.goodreads.com/search.xml?key=sBITGRylosZkjIAaixQ&q=Ender%27s+Game')


print response
