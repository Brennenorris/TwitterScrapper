from selenium import webdriver

# Specify the path to ChromeDriver
chrome_driver_path = '/desktop/WebScraper/chromedriver_mac_arm64'  

# Initialize the WebDriver with the path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the Twitter Explore page
explore_url = "https://twitter.com/explore/tabs/trending"
driver.get(explore_url)

# Find and extract the links for the top 15 trending topics
trending_topics = driver.find_elements_by_css_selector('div.css-1dbjc4n a')

# Iterate through the first 15 trending topics and print their links
for topic in trending_topics[:15]:
    trend_name = topic.text
    trend_link = topic.get_attribute('href')
    print(f"{trend_name}: {trend_link}")

# Close the web browser
driver.quit()
