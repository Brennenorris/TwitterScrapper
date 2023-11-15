from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Specify path to ChromeDriver
chrome_driver_path = 'c:\Users\brenn\OneDrive\Desktop\Void\chromedriver.exe'  

# Initialize WebDriver with path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Twitter URL 
tweet_url = 'website_url'

driver.get(tweet_url)

wait = WebDriverWait(driver, 10)  #timeout

#likes
likes_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 span')))
likes = likes_element.text

#retweets 
retweets_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 span')))
retweets = retweets_element.text

#views
views_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1t68eav span')))
views = views_element.text

#post time 
post_time_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'time')))
post_time = post_time_element.get_attribute('datetime')

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Use the configuration settings to set the variables in your script
website_url = config['website_url']
pages_to_scrape = config['pages_to_scrape']
data_to_extract = config['data_to_extract']
data_output_file = config['data_output_file']
run_program = config['run_program']

if run_program:
    # Your web scraping logic here
    print(f"Scraping {pages_to_scrape} pages from {website_url}")
    print(f"Extracting data: {data_to_extract}")
    print(f"Saving data to {data_output_file}")
else:
    print("Program is off Set 'run_program' to true in config to enable")
