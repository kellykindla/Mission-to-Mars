# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

#import pandas 
import pandas as pd

#set your executable path and url 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
#searching for elements with tag div and attribute list_text
# telling our browser to wait one second before searching for components 
browser.is_element_present_by_css('div.list_text', wait_time=1)

#set up html parser 
html = browser.html
news_soup = soup(html, 'html.parser')
#create slide_elem to search for the <div /> tag 
slide_elem = news_soup.select_one('div.list_text')

#begin scraping by chaining find onto slide_elem to find specific data (class = "content_title")
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title` to get the title alone 
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Image from JPL Space Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button - clicks the second button tag
full_image_elem = browser.find_by_tag('button')[1]
#splinter will click the image
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
#get('src') pulls the link to the most recent image 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts Table 

#set up code to retrieve table of mars facts 
#create a dataframe from the first html table- index 0
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#create/specify columns 
df.columns=['description', 'Mars', 'Earth']
#set the description column as the index 
df.set_index('description', inplace=True)
df


#convert dataframe back to html ready code 
df.to_html()

#end session 
browser.quit()


