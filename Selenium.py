from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import os
import time

parser = argparse.ArgumentParser('Parser for the new project maker right!')

parser.add_argument('repo', type=str, help="The name of the new project.")

args = parser.parse_args()

REPO_NAME = args.repo

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome()#options=options)
driver.get('https://github.com/login')

username = driver.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys('YOUR EMAIL HERE')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('YOUR PASSWORD HERE')

login = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
login.click()

new_repo = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
new_repo.click()

repo_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name.send_keys(REPO_NAME)

time.sleep(1)
make_repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
make_repo.click()
