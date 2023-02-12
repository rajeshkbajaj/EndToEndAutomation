from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from Library import ConfigReader


def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    driver.find_element(By.NAME,ConfigReader.fetchElementLocators("Registration","password_name")).send_keys("abcd")
    driver.close()