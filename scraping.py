# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

#create a function to initialize browser, create data dictionary, and end webdriver 
def scrape_all():
#set your executable path and url 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "hemisphere_images_urls": hemispheres(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

#create mars_news function to get the title and summary 
def mars_news(browser):
    #scrape mars news 
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
    
    #add try/except for error handling 
    try: 
        #create slide_elem to search for the <div /> tag 
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title` to get the title alone 
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    #if code runs into an AttributeError, python will return nothing 
    except AttributeError:
        return None, None 

    return news_title, news_p

#create featured_image function to scrape for image 
def featured_image(browser): 
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

    try: 
        # Find the relative image url
        #get('src') pulls the link to the most recent image 
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

#create mars_facts() function 
def mars_facts(): 
    # ### Mars Facts Table 
    try: 
        #set up code to retrieve table of mars facts 
        #create a dataframe from the first html table- index 0
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    #create/specify columns 
    df.columns=['Description', 'Mars', 'Earth']
    #set the description column as the index 
    df.set_index('Description', inplace=True)

    #convert dataframe back to html ready code and return it 
    return df.to_html(classes="table table-striped")

#create hemisphres function
def hemispheres(browser):
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for x in (4, 6, 8, 10):
        
        #find and click the link to full-res imgae
        full_res_image = browser.find_by_tag('a')[x]
        full_res_image.click()
        
        #create an empty dictionary to hold image and title 
        hemispheres = {}
        
        #parse the full_res_image html
        html = browser.html
        full_res_img_soup = soup(html, 'html.parser')
        
        
        #get the url link for the image
        full_res_image_div = full_res_img_soup.find('div', class_ = "downloads")
        full_res_image_jpeg = full_res_image_div.find('a').get('href')
            
        # Use the base URL to create an absolute URL
        full_res_img_url = f'https://marshemispheres.com/{full_res_image_jpeg}'
            
        #add url to dictionary as key
        hemispheres['img_url'] = full_res_img_url
            
        #find the title 
        find_title = full_res_img_soup.find('div', class_='cover')
        img_title = find_title.find('h2', class_="title").text
            
        #add title to dictionary as value
        hemispheres['title'] = img_title
            
        #append hemispheres dictionary to list 
        hemisphere_image_urls.append(hemispheres)
            
        #return to beginning to get next image 
        browser.back()
    
    # 4. return the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

#tell flask that our script is complete 
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

