import pytest
from selenium import webdriver
import allure
import openpyxl
import EventExcel
import time

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()

def readData():
    list = []
    path = "O:\Testdata1.xlsx"

    rows = EventExcel.getRowCount(path, 'Sheet1')

    for r in range(2, rows + 1):
        username = EventExcel.readData(path, "Sheet1", r, 1)
        password = EventExcel.readData(path, "Sheet1", r, 2)

        tuple = (username, password)
        list.append(tuple)

    print(list)
    return list

@allure.description("Validate Tpos with valid login ")
@allure.severity(severity_level="CRITICAL")
@pytest.mark.parametrize("username, password", readData())
def test_validLogin(test_setup, username, password):
    driver.get("https://tmt30.tpos.vn/#/account/login")
    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").clear()
    enter_username(username)
    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").clear()
    enter_password(password)

    driver.find_element_by_css_selector("[type='submit'][class='btn btn-lg btn-primary btn-block']").click()
    time.sleep(5)
    try:
        assert "dashboard" in driver.current_url
        print("Testcase Pass")
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name="Tài khoản đăng nhập không đúng", attachment_type=allure.attachment_type.PNG)
            print("Testcase Pass")

@allure.step("Entering username as {0}")
def enter_username(username):
    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").send_keys(username)

@allure.step("Entering password as {0}")
def enter_password(password):
    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").send_keys(password)




