from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
chrome_driver_path = r'C:\Users\xstam\chromedriver-win64\chromedriver.exe'

# Initialize the Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open YouTube


# Wait for the page to load
# Function to remove ads
def remove_ads():
    driver.get('https://www.youtube.com')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    while True:
        try:
            # Find and remove ad elements
            ads = driver.find_elements(By.CSS_SELECTOR, '.video-ads, .ytp-ad-module, .ytp-ad-overlay-container')
            for ad in ads:
                driver.execute_script("""
                    var element = arguments[0];
                    element.parentNode.removeChild(element);
                """, ad)
            #time.sleep(2)  # Check for ads every 5 seconds
        except Exception as e:
            print(f"Error: {e}")

# Start removing ads
