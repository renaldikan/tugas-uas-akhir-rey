#melihat semua informasi user pada sub menu yang ada pada menu My info

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
    

def test_my_info_name(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.NAME, 'username').send_keys("Admin")
    driver.find_element(
        By.NAME, 'password').send_keys("admin123"+ Keys.ENTER)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewPersonalDetails/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/contactDetails/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewEmergencyContacts/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewDependents/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewImmigration/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewJobDetails/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewSalaryList/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewUsTaxExemptions/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewReportToDetails/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewQualifications/empNumber/7"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/pim/viewMemberships/empNumber/7"]').click()
    sleep(1)
   
