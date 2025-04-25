from selenium import webdriver
# import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# This code is a simple example of how to use Selenium to automate a web browser.
# It opens a web page, finds an element by its ID, and prints the text of that element.
# It also demonstrates how to use the By class to locate elements using different strategies.

#Create a new instance of the chrome driver
driver = webdriver.Chrome()

#fetch data using id from amazon.in
driver.get("https://www.walmart.com/ip/Better-Homes-Gardens-Brookbury-4-Piece-Outdoor-Wicker-Patio-Sectional-Dining-Set-Brown/3766266617?classType=VARIANT&athbdg=L1600")

product=driver.find_element(By.ID, "main-title")
price = driver.find_element(By.XPATH, "//span[@itemprop='price']").text.strip()
brand=driver.find_element(By.XPATH, "//h3[text()='Brand']/following-sibling::div/span")
# model_no=driver.find_element(By.CLASS_NAME, "mv0 lh-copy mid-gray f6")
try:
    if product:
        print("Product Title:", product.text)
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
    # if model_no:    
    #     print("Model Number:", model_no.text.strip())
    # else:   
    #     print("Model Number not found")
except NoSuchElementException:
    print("Element not found")
    print("Element not found")
# except TimeoutException:  
except Exception as e:
    print("Error:", e)

time.sleep(5)
# Close the browser
driver.quit()
#     if price:
#     if brand:
#         print("Brand:", brand)          
#     else:
#         print("Product Title not found")
#     if model_no:    
#         print("Model Number:", model_no)
#     else:
#         print("Model Number not found")
# except Exception as e:
#     print("Error:", e)
# Find the element with the ID "nav-search-submit-button"