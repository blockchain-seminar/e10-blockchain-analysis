from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
import logging

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# from X2Y2
def get_nft_links():
    driver.get("https://x2y2.io/collections")

    time.sleep(5)

    # switch to 7d view
    driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/ul/li[5]/button").click()

    links = []

    for j in range(1,4):
        time.sleep(5)
        for i in range(1,100):
            try:
                xpath = f"//*[@id=\"__next\"]/div[1]/section/ul/li[{i}]/div[1]/div/div[1]/a"
                element = driver.find_element(By.XPATH, xpath)
                links.append(element.get_attribute('href'))
            except Exception as e:
                print(f"Could not fetch data for item {i}: {e}")

        # continue to next
        forward_btn = 1 if j < 2 else 2
        continue_page = f"//*[@id=\"__next\"]/div[1]/section/nav/button[{forward_btn}]"
        driver.find_element(By.XPATH, continue_page).click()

    return links

def get_nft_address(link):
    driver.get(link)

    time.sleep(5)

    contr_address = "//*[@id=\"__next\"]/div[1]/header/div[1]/div[1]/div/div/button[1]"
    nft_name = "//*[@id=\"__next\"]/div[1]/header/div[1]/div[1]/div[2]/div[1]/div[2]/h1"
    driver.find_element(By.XPATH, contr_address).click() # address stored in clipbaord
    name = driver.find_element(By.XPATH, nft_name).text
    return {'address': pyperclip.paste(), 'nft': name} # returns the contract address


logging.basicConfig(filename='./data/nft_addresses.log', level=logging.INFO)

links = get_nft_links()
for link in links:
    logging.info(get_nft_address(link))

driver.quit()