from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException


def parsing_tt(urls):

    data = {"objects": []}
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(service=service, options=options)
    stealth(driver=browser,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/83.0.4103.53 Safari/537.36',
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            run_on_insecure_origins=True,
            )
    browser.set_window_size(1000, 1000)
    data_url = {}
    for url in urls:
        browser.get(url)
        data_url = {"url": url}
        videos = browser.find_elements(By.CLASS_NAME, "tiktok-x6y88p-DivItemContainerV2")
        for video in videos:
            time.sleep(5)
            views = video.find_element(By.CLASS_NAME, "video-count").text
            print(views)
            try:
                badge = video.find_element(By.CLASS_NAME, "tiktok-3on00d-DivBadge")
                continue
            except NoSuchElementException:
                video.click()
                date_create = browser.find_element(By.XPATH, "//span[@class = 'tiktok-gg0x0w-SpanOtherInfos']/span[3]").text
                print(date_create)
                browser.execute_script("window.history.go(-1)")
        time.sleep(40)


    browser.quit()
    return data

if __name__ == "__main__":
    parsing_tt(["https://www.tiktok.com/@wj.amjk_"])