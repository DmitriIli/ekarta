from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time, os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


def get_parse_data():
    load_dotenv()
    # options
    os.getenv('login')
    options = webdriver.ChromeOptions()
    ua = UserAgent(browsers=['chrome'])
    options.add_argument(f'user-agent={ua.random}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        options=options
    )

    try:
        url = 'https://deti.cdsvyatka.com/#/login'
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(1)
        id_field = driver.find_element(By.NAME, 'login')
        password_field = driver.find_element(By.NAME, 'password')
        id_field.clear()
        password_field.clear()
        id_field.send_keys(os.getenv('login'))
        password_field.send_keys(os.getenv('password'))
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        button = driver.find_element(By.CLASS_NAME, 'v-form').find_element(By.TAG_NAME, 'button')
        button.click()
        time.sleep(1)
        url = 'https://deti.cdsvyatka.com/#/events'
        driver.get(url=url)
        time.sleep(1)
        subject = driver.find_elements(
            By.XPATH, "//div[contains(text(),'Карта ')]")[0]
        data = driver.find_elements(
            By.XPATH, "//div[@class='v-list__tile__content']/div[@class='v-list__tile__sub-title']")[0]
        return (subject.text, data.text)

    except Exception as ex:
        return ('errore')
    finally:
        driver.close()
        driver.quit()
