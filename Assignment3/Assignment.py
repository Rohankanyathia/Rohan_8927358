from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Selenium driver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

# Open Google website
driver.get("https://www.google.com")

# Find and interact with the search input field
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_input.send_keys("how to use ChatGPT video")
search_input.submit()

# Find and interact with the YouTube video link
youtube_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.g:nth-child(1) a[href^='https://www.youtube.com']"))
)
youtube_link.click()

# Wait for the video to load
time.sleep(5)

# Skip the YouTube ad
skip_ad_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button"))
)
skip_ad_button.click()

# Play the video for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
