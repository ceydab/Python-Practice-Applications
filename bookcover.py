
from bs4 import BeautifulSoup
import requests
import pymongo
import matplotlib.pyplot as plt
import re
import pandas as pd


'''
This project aims to look into booklists on goodreads on book cover colors and see if there is any correlation
between cover color and reading number, genre, rate. To do this, the project uses the below linked lists and scraps
information about a hundred books on each list to create a table on title, author, rating number, rate, color.
Once the table is completed, the aim is to compare the data and see which color is preferred the most by checking
the rating number and rate by taking the mean value. BookInfo will create a database including said columns. Compare 
will use pandas to compare the values.

Blue = "https://www.goodreads.com/list/show/15500.In_Love_With_BLUE_Covers_"
Red = "https://www.goodreads.com/list/show/2959.Seeing_Red"
Black = "https://www.goodreads.com/list/show/2973.Great_Books_with_BLACK_Covers"
Yellow = "https://www.goodreads.com/list/show/2784.Yellowest_Books_Ever"
Green = "https://www.goodreads.com/list/show/2948.Greenest_Books_Ever"
White = "https://www.goodreads.com/list/show/3056.White_as_the_Driven_Snow"
Pink = "https://www.goodreads.com/list/show/2958.In_the_Pink" 
Purple = "https://www.goodreads.com/list/show/2922.The_Color_Purple"
Gray = "https://www.goodreads.com/list/show/2977.Grey_Daze"
'''

class BookInfo():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client["app"]
        self.collection = self.db["books"]

        blue = "https://www.goodreads.com/list/show/15500.In_Love_With_BLUE_Covers_"
        red = "https://www.goodreads.com/list/show/2959.Seeing_Red"
        black = "https://www.goodreads.com/list/show/2973.Great_Books_with_BLACK_Covers"
        yellow = "https://www.goodreads.com/list/show/2784.Yellowest_Books_Ever"
        green = "https://www.goodreads.com/list/show/2948.Greenest_Books_Ever"
        white = "https://www.goodreads.com/list/show/3056.White_as_the_Driven_Snow"
        pink = "https://www.goodreads.com/list/show/2958.In_the_Pink" 
        purple = "https://www.goodreads.com/list/show/2922.The_Color_Purple"
        gray = "https://www.goodreads.com/list/show/2977.Grey_Daze"
        
        self.url = [blue, red, black, yellow, green, white, pink, purple, gray]
        self.covercolor = ["blue", "red", "black", "yellow", "green", "white", "pink", "purple", "gray"]
        
        for r,s in zip(self.url, self.covercolor):
            self.url = r
            self.covercolor = s

            self.html = requests.get(self.url).content
            self.soup = BeautifulSoup(self.html, "html.parser")
            
            self.getbook()
    

    def getbook(self):
    
        
        i = 0
        while 100 > i:
            self.bookno = self.collection.count_documents({})
            self.title = self.soup.find_all('a', 'bookTitle')[i].get_text()
            self.author = self.soup.find_all('a', 'authorName')[i].get_text()
            rateinfo = self.soup.find_all('span','minirating')[i].get_text()
            self.ratedfor = int(re.split(" ", rateinfo)[5].replace(",",""))
            self.rate = float(re.split(" ", rateinfo)[1])
            self.createTable()
            i+=1
    
    def createTable(self):
        
        book = {
            "_id" : self.bookno + 1,
            "name" : self.title,
            "author" : self.author,
            "ratedfor" : self.ratedfor,
            "rate" : self.rate,
            "cover" : self.covercolor
            }
        self.collection.insert_one(book)        
                      

class Compare():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client["app"]
        self.collection = self.db["books"]
        self.organize()

    def organize(self):
        bookspd = pd.DataFrame(self.collection.find({}))
        self.covergrouped = bookspd.groupby(["cover"])
        self.coverratemean = pd.Series(self.covergrouped.mean()["rate"])
        self.coverratedformean = pd.Series(self.covergrouped.mean()["ratedfor"])
        self.covergroupedcolors = self.covergrouped.groups.keys()

        self.visualise()

    def visualise(self):
        covervsrate = plt.bar(self.covergroupedcolors, self.coverratemean, label = "colors", width=0.8)
        plt.show()
        covervsratedfor = plt.bar(self.covergroupedcolors, self.coverratedformean, label = "colors", width=0.8)
        plt.show()

        '''
        This function plots the graphs rate vs color and rated for number vs color. The result is that black colored books are the most rated,
        whereas green colored books have the highest rate with blue following.
        '''
        
            
            
            

BookInfo()
Compare()