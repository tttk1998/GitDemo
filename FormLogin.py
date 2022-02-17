import EventExcel
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win23\chromedriver.exe")

driver.get("https://tmt30.tpos.vn/#/account/login")
time.sleep(5)
#driver.maximize_window()

path="E:\Testdata1.xlsx"

rows=EventExcel.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    text=EventExcel.readData(path,"Sheet1",r,1)
    password=EventExcel.readData(path,"Sheet1",r,2)

    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").send_keys(text)

    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").send_keys(password)

    driver.find_element_by_css_selector("[type='submit'][class='btn btn-lg btn-primary btn-block']").click()

    time.sleep(5)

    img = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/ul[2]/li[6]/a/span/img")
    driver.execute_script("arguments[0].click();", img)

    time.sleep(5)

    driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/ul[2]/li[6]/ul/li[3]/a").click()


    if driver.title=="TPOS":
        print("test is passed")
        break
        #EventExcel.WriteData(path,"Sheet1",r,3,"test passed")
    else:
        print("test is failed")
        driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").clear()

        driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").clear()
        #EventExcel.WriteData(path,"Sheet1",r,3,"test failed")

    time.sleep(5)

    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").send_keys(Keys.F5)
