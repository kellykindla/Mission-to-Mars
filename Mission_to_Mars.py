#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

#import pandas 
import pandas as pd


# In[2]:


#set your executable path and url 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
#searching for elements with tag div and attribute list_text
# telling our browser to wait one second before searching for components 
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#set up html parser 
html = browser.html
news_soup = soup(html, 'html.parser')
#create slide_elem to search for the <div /> tag 
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


#begin scraping by chaining find onto slide_elem to find specific data (class = "content_title")
slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title` to get the title alone 
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button - clicks the second button tag
full_image_elem = browser.find_by_tag('button')[1]
#splinter will click the image
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
#get('src') pulls the link to the most recent image 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts Table 

# In[14]:


#set up code to retrieve table of mars facts 
#create a dataframe from the first html table- index 0
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#create/specify columns 
df.columns=['description', 'Mars', 'Earth']
#set the description column as the index 
df.set_index('description', inplace=True)
df


# In[15]:


#convert dataframe back to html ready code 
df.to_html()


# In[16]:


#end session 
browser.quit()


# In[ ]:




