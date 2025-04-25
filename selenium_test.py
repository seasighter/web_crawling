from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# This code is a simple example of how to use Selenium to automate a web browser.
# It opens a web page, finds an element by its ID, and prints the text of that element.
# It also demonstrates how to use the By class to locate elements using different strategies.

#Create a new instance of the chrome driver
driver = webdriver.Chrome()
#fetch data using id from amazon.in
driver.get("https://www.flipkart.com/fastrack-optimus-pro-1-43-amoled-display-aod-466x466-functional-crown-bt-calling-smartwatch/p/itma4744c9053b72?pid=SMWGV3ZY9YJYEYEC&lid=LSTSMWGV3ZY9YJYEYECZN6QCW&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_3&otracker=browse&fm=organic&iid=5faea34c-0763-43fc-b0fc-56eef5a6bf2c.SMWGV3ZY9YJYEYEC.SEARCH&ppt=hp&ppn=homepage&ssid=yga84lcz0g0000001745558914798")
# Find the element with the ID "nav-search-submit-button"
product_title = driver.find_element(By.CLASS_NAME, "VU-ZEz")

price = driver.find_element(By.XPATH, "//div[contains(@class, 'Nx9bqj')]")
print("Discounted Price:", price.text.strip())
print("Product Title:", product_title.text)
# Wait for a few seconds to see the result
time.sleep(5)


# Close the browser
driver.quit()


