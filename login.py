import pytest
from selenium import webdriver
import allure
import openpyxl
import EventExcel

def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win23\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    #yield
    driver.quit()
test_setup()

def test_validLogin():
    driver.get("https://tmt30.tpos.vn/#/account/login")
    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").clear()
    enter_username("admin")
    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").clear()
    enter_password("123123@")

    driver.find_element_by_css_selector("[type='submit'][class='btn btn-lg btn-primary btn-block']").click()
    assert "dashboard" in driver.current_url
test_validLogin()

def test_invalidLogin():
    driver.get("https://tmt30.tpos.vn/#/account/login")
    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").clear()
    enter_username("thanhkieu")
    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").clear()
    enter_password("123456")

    driver.find_element_by_css_selector("[type='submit'][class='btn btn-lg btn-primary btn-block']").click()

    try:
        assert "dashboard" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name="Tài khoản đăng nhập không đúng", attachment_type=allure.attachment_type.PNG)
test_invalidLogin()

#@allure.step("Entering username as {0}")
def enter_username(username):
    driver.find_element_by_css_selector("[type='text'][placeholder='Tên tài khoản']").send_keys(username )
enter_username()

#@allure.step("Entering password as {0}")
def enter_password(password):
    driver.find_element_by_css_selector("[type='password'][placeholder='Mật khẩu']").send_keys(password)
enter_password()

