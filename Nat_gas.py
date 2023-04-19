from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
folder_name = "\_Output"
def download_file(chromedriver_url):
     path = DIR_PATH
     options = webdriver.ChromeOptions();
     prefs = {"download.default_directory": path};
     options.add_experimental_option("prefs", prefs);
     driver = webdriver.Chrome(service_log_path=chromedriver_url, options=options)
     driver.get("https://www.cores.es/en/estadisticas")
     driver.maximize_window()
     time.sleep(5)
     driver.find_element(By.CSS_SELECTOR, "a[title='gas-imports.xlsx']").send_keys(Keys.ENTER)
     time.sleep(5)
     driver.close()

def process_file():
    path=os.path.abspath('gas-imports.xlsx')
    df=pd.read_excel(path,sheet_name='Africa',usecols='A:Q',header=5)
    df=df.loc[:248]
    path = os.path.join(DIR_PATH, folder_name)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    df.to_csv(os.path.join(path,'Gas-Imports.csv'),index=False)

download_file("D:/selenium/chromedriver.exe")
process_file()

