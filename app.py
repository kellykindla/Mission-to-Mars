#import necessary tools 
#use flask to render a template, redirecting to another url, and creating a url 
from flask import Flask, render_template, redirect, url_for
#use pymongo to interact with mongo db
from flask_pymongo import PyMongo
#use scrapping code (convert from jupyter notebook to python)
import scraping

#set up flask 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#our app will connect to mongo with a URI 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define route for html page 
@app.route("/")
def index():
    #use mongo to find the "mars" collection in our database 
   mars = mongo.db.mars.find_one()
   #tells flask to return an HTML template using an index.html file 
   return render_template("index.html", mars=mars)

#set up scraping route/ button of the web application 
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   #access the database and scrape data with scraping.py script 
   #mars_data will hold the scraped data 
   mars_data = scraping.scrape_all()
   #update database- insert data but not if an identical record exists 
   #upsert = True will create a new document if one doesn't exist 
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   #will navigate our page back to home to see updated content 
   return redirect('/', code=302)

#tell flask to run 
if __name__ == "__main__":
   app.run()