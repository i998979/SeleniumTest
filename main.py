import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless") #無頭模式
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"})
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/SabrinaPingpingNG")
print(driver.page_source)
