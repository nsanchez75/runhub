from selenium import webdriver
from selenium.webdriver.common.by import By

city = input("What city are you currently in? \n")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.visualcrossing.com/weather/weather-data-services")

# accept cookies
driver.find_element(By.XPATH, "//button[@class='btn btn-sm btn-primary col-lg-3']").click()

# search bar
driver.find_element(By.XPATH, "//input[@class='form-control border-end-0 border-primary']").send_keys(city)
