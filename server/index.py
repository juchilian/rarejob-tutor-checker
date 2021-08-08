import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.CHROME
)
driver.implicitly_wait(5)

driver.get("https://www.rarejob.com/account/login/")

print(driver.title)
driver.quit()
    

