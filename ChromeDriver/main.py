from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
from authdata import login, password
from selenium.webdriver.common.by import By


# options
ENTER = '\eu007'
options = webdriver.ChromeOptions()
ua = UserAgent(browsers=['chrome'])
options.add_argument(f'user-agent={ua.random}')
options.add_argument("--disable-blink-features=AutomationControlled")
# url ='https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
url = 'https://deti.cdsvyatka.com/#/login'
driver = webdriver.Chrome(
    options=options
)
try:
    
    driver.get(url=url)
    # driver.implicitly_wait(10)    
    driver.maximize_window()
    driver.get(url=url)
    id_field = driver.find_element(By.NAME, 'login')
    password_field = driver.find_element(By.NAME, 'password')
    id_field.clear()
    password_field.clear()
    id_field.send_keys(login)
    password_field.send_keys(password)
    time.sleep(3)
    button = driver.find_element(By.CLASS_NAME, 'v-form').find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(3)
    url = 'https://deti.cdsvyatka.com/#/events'
    driver.get(url=url)
    time.sleep(5)
    subject = driver.find_elements(By.XPATH, "//div[contains(text(),'Карта ')]")[0]

    data = driver.find_elements(By.XPATH, "//div[@class='v-list__tile__content']/div[@class='v-list__tile__sub-title']")[0]
    
    print(subject.text , data.text)
    
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
