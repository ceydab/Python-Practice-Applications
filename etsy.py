#extract data from the given link and create a database

from selenium import webdriver
import time
import pymongo
import requests
from bson.objectid import ObjectId



class productTable():
    def __init__(self):
        print('x')
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client["app"]
        self.collection = self.db["products"]
        self.listing = self.collection.find({"from":"etsy"})
        self.count = self.collection.count_documents({"from":"etsy"})
        
        self.choice()
    
    def choice(self):
        print("1- Add new product\n"  "2- Show a product\n" "3- List all products")
        choice = input("What do you want to do?:")

        if choice == '1':
            self.createTable()
        elif choice =='2':
            self.getProductbyId()
        elif choice =='3':
            self.listProducts()
        else:
            print("No such choice. Choose again")
            self.choice()

    def createTable(self):
        url = input("Link to the product: ")
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        productTitle = driver.title
        productPrice = driver.find_element('xpath',"//*[@id='listing-page-cart']/div[3]/div[1]/div[1]/div[1]/div[1]/div/div[1]/p" ).text
        productImage = driver.find_element('xpath',"//*[@id='listing-right-column']/div/div[1]/div[1]/div/div/div/div/div[1]/ul/li[1]/img").get_attribute("src")
        time.sleep(2)
        driver.close()
        
        product = {
            "_id" : self.count +1,
            "name" : productTitle,
            "image" : productImage,
            "price" : productPrice,
            "from" : "etsy"
        }
        
        result = self.collection.insert_one(product)
        insertedProductId = result.inserted_id

        findInsertedProduct = self.collection.find({"_id" : ObjectId(insertedProductId)})
        for i in findInsertedProduct:
            
            print(i)
        
    
    def getProductbyId(self):
        desiredId = input("Enter Id: ")
        result = self.collection.find({"_id" : int(desiredId)})
        for i in result:
            print(i)


    def listProducts(self):
        result = self.collection.find()
        for i in result:
            print([i])


productTable()