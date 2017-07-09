from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://github.com")
#assert "Python" in driver.title
elem = driver.find_elements_by_name("q")
print(elem)
elem.send_keys("weixin")
elem.send_keys(Keys.RETURN)
print(driver.page_source)