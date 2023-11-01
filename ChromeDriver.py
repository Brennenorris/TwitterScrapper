from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to ChromeDriver
chrome_driver_path = '/path/to/chromedriver'  # Replace with the actual path to chromedriver

# Set the download directory for Chrome
download_directory = '/path/to/download_directory'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()

# Set the download directory
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_directory,
    'download.prompt_for_download': False,  # Optional: Disable download prompts
    'download.directory_upgrade': True,  # Optional: Directory upgrade prompt
    'safebrowsing.enabled': False,  # Optional: Disable safe browsing
})

# Initialize the ChromeDriver with options
driver = webdriver.Chrome(
    executable_path=chrome_driver_path,
    options=chrome_options
)

# Now you can use the driver to navigate, interact with web pages, and handle downloads.

# For example, to navigate to a website:
driver.get('https://example.com')

# Rest of your code for web scraping, interaction, or navigation

# Don't forget to close the driver when you're done
driver.quit()
