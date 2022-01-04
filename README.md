# Mission to Mars
## Module 10 

## Project Overview 
### Purpose of Module 10 
In this module, we were introduced to multiple web scraping tools in efforts to extract data from appropriate websites and ultimately, create a web app of our own. For this module, we used chrome developer tools to identify HTML components to use along with BeautifulSoup and Splinter to scrape data for analysis. We were also introduced to Mongo to create a database instance to store our non-structured data. We then further developed our web application development skills through the use of flask and Bootstrap to put our findings into one comprehensive location. 

### Overview of Assignment 
For this assignment, we were asked to write a script that gathers the most recent information on mars and publish our findings to a central location- a webpage. The data we scraped includes the latest Mars news, a featured Mars image, a table of Mars facts, and the four most recent Mars hemisphere images. Our script was written to be updated with new data by simply clicking the “scrape new data” button of our responsive web application. We then added additional flare by using bootstrap and CSS components to make the web app our own. 

### Resources 
#### The websites used to scrape data are: 
	- Latest Mars News: 'https://redplanetscience.com'
	- Featured Mars Image: 'https://spaceimages-mars.com'
	- Mars Facts: 'https://galaxyfacts-mars.com'
	- Mars Hemispheres : 'https://marshemispheres.com/'
#### Software and Dependencies: 
	- Python 7.22.0
	- VS Code 1.62.1 
	- Splinter 0.16.0
	- Web Driver Manager Package 3.5.2
	- BeautifulSoup bs4-0.0.1
	- PyMongo 4.0.1
	- Flask 2.3.0
	- html5lib 1.15.0
	- lxml 4.6.3
	- Pandas 

### Results 
The following image is my final web application. It contains the latest NASA news pertaining to Mars and can be updated with the “Scrape New Data” button. The bootstrap changes I made were:  replacing the jumbotron header with a web image, changed button color, changed the title color for each header, added thumbnails to the Mars Hemisphere images, and changed the body background color. 
<img width="589" alt="Screen Shot 2022-01-03 at 7 26 35 PM" src="https://user-images.githubusercontent.com/92558842/147999350-fae25345-da8a-425a-8304-efabfe9e8fcb.png">
