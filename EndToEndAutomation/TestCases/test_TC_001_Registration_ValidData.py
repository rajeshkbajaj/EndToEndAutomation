import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
from DataGenerate import DataGen

@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    #register.enter_email('abcd')
    #driver.find_element(By.NAME,ConfigReader.fetchElementLocators("Registration","username_name")).send_keys("hello")
    #driver.find_element(By.NAME,ConfigReader.fetchElementLocators("Registration","email_name")).send_keys("abcd")
    driver.close()
