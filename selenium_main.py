from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = ChromeDriverManager().install()
options = ChromeOptions()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service, options=options)


def wait_element(browser, delay_second=1, by=By.CLASS_NAME, value=None):

    return WebDriverWait(browser, delay_second).until(
        EC.presence_of_element_located((by, value))
    )
