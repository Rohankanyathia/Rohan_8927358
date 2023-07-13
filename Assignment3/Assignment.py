from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Flipkart homepage
driver.get("https://www.flipkart.com")
time.sleep(3)

# Handling login popup if it appears
try:
    close_button = driver.find_element("xpath", "//button[@class='_2KpZ6l _2doB4z']")
    close_button.click()
    time.sleep(2)
except:
    pass

# Finding the search bar and entering text
search_bar = driver.find_element("xpath", "//input[@class='_3704LK']")
search_bar.send_keys("iPhone 14 Pro")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "iPhone 14 Pro" in driver.title

# Selecting the iPhone 14 Pro from the search results
iphone_link = driver.find_element("xpath", "//a[@class='_1fQZEK']")
iphone_link.click()

# Waiting for the iPhone details page to load
time.sleep(5)

# Adding the iPhone to the cart
add_to_cart_button = driver.find_element("xpath", "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Verifying that the iPhone has been added to the cart
cart_count = driver.find_element("xpath", "//span[@class='_10Ermr']")
assert cart_count.text == "1"

# Closing the webdriver
driver.close()
