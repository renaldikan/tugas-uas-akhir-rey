#Add Employee pada menu PIM

import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant
import utils

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield driver
    

def test_add_employee(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.NAME, 'username').send_keys("Admin")
    driver.find_element(
        By.NAME, 'password').send_keys("admin123"+ Keys.ENTER)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()
    driver.find_element(
        By.XPATH, '//li[@class="oxd-topbar-body-nav-tab"]').click()
    sleep(2)
    driver.find_element(
        By.NAME, 'firstName').send_keys("Adhit")
    sleep(1)
    driver.find_element(
        By.NAME, 'middleName').send_keys("Thana")
    sleep(1)
    driver.find_element(
        By.NAME, 'lastName').send_keys("Mahiddhika")
    sleep(1)
    driver.find_element(
    By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
    sleep(3)