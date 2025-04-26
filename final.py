from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import random

# Create a new instance of the Chrome driver
option=Options()
option.add_argument("window-size=1920,1080")  
driver = webdriver.Chrome(options=option)
# Step 1: Fetch data from Walmart
driver.get("https://www.walmart.com/ip/Better-Homes-Gardens-Brookbury-4-Piece-Outdoor-Wicker-Patio-Sectional-Dining-Set-Brown/3766266617?classType=VARIANT&athbdg=L1600")

time.sleep(random.randint(2, 5))  # Instead of fixed 2-3 sec

try:
    product = driver.find_element(By.ID, "main-title")
    price = driver.find_element(By.XPATH, "//span[@itemprop='price']").text.strip()
    brand = driver.find_element(By.XPATH, "//h3[text()='Brand']/following-sibling::div/span")

    if product:
        product_title = product.text
        print("Product Title:", product_title)
    else:
        print("Product Title not found")
    
    if price:
        print("Discounted Price:", price)
    else:
        print("Discounted Price not found")
    
    if brand:
        print("Brand:", brand.text.strip())
    else:
        print("Brand not found")

except NoSuchElementException:
    print("Element not found on Walmart page")
except Exception as e:
    print("Error:", e)

# Step 2: Search the product title on Google
try:
    driver.get("https://www.google.com/")
    time.sleep(random.randint(2, 5))  # Instead of fixed 2-3 sec

    search_box = driver.find_element(By.NAME, "q")  # Google's search box
    search_box.send_keys(product_title + " site:amazon.com")  # Focus on Amazon results
    search_box.send_keys(Keys.RETURN)  # Press Enter
    time.sleep(3)

    # Step 3: Click the first Amazon link if available
    amazon_link = driver.find_element(By.XPATH, "//a[contains(@href, 'amazon.com')]")
    amazon_url = amazon_link.get_attribute('href')
    print("Amazon URL Found:", amazon_url)

    # Open the Amazon page
    driver.get(amazon_url)

except NoSuchElementException:
    print("No Amazon link found in search results")
except Exception as e:
    print("Error during Google search:", e)

# Step 4: (Optional) Add sleep to see the Amazon page
time.sleep(5)

# Close the browser
driver.quit()
