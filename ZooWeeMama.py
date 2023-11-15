from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import json

# Specify path to ChromeDriver
chrome_driver_path = 'c:\\Users\\brenn\\OneDrive\\Desktop\\Void\\chromedriver.exe'  

# Initialize WebDriver with path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Twitter URL 
tweet_url = 'https://twitter.com/search?q=%22Michael%20Burry%22&src=trend_click&vertical=trends'

driver.get(tweet_url)

wait = WebDriverWait(driver, 10)  # Timeout

# Extract data
tweet_id_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweet']")))
tweet_id = tweet_id_element.get_attribute("data-tweet-id")

tweet_text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 div')))
tweet_text = tweet_text_element.text

timestamp_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'time')))
timestamp = timestamp_element.get_attribute('datetime')

likes_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 span')))
likes = likes_element.text

retweets_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 span')))
retweets = retweets_element.text

hashtags_elements = driver.find_elements(By.CSS_SELECTOR, '.css-901oao.r-111h2gw.r-1qd0xha.r-1b6yd1w.r-1vr29t4.r-1v8dza6.r-bcqeeo.r-qvutc0 span')
hashtags = ', '.join([element.text for element in hashtags_elements])

source_url_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 a')))
source_url = source_url_element.get_attribute('href')

user_location_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-1re7ezh.r-1qd0xha.r-n6v787.r-16dba41.r-1sf4r6n.r-bcqeeo.r-qvutc0 span')))
user_location = user_location_element.text

mysql_config = {
    "host": "localhost",
    "user": "root",
    "password": "sesJOc-kIlmN",
    "database": "Local_instance_MySQL80",
    "port": 3306
}

# Connect to MySQL database
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Insert data into the MySQL table
insert_query = """
    INSERT INTO twitter_data (
        tweet_id, tweet_text, timestamp, likes, retweets, hashtags, source_url, user_location
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
data = (
    int(tweet_id), tweet_text, timestamp, int(likes), int(retweets), hashtags, source_url, user_location
)
cursor.execute(insert_query, data)

# Commit the changes and close the connection
conn.commit()
conn.close()

driver.quit()
