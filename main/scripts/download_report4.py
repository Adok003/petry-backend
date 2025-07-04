from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://aisoip.adilet.gov.kz/main")

cookie_path = "steps/cookies.json"
url = "https://aisoip.adilet.gov.kz/main"

driver.get(url)

time.sleep(100)

driver.quit()