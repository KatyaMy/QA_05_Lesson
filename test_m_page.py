import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/'


class TestMainPage():
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_1(self):
        self.driver.get(link)

    def test_2(self):
        self.driver.get(link)
        self.driver.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()





# class TestMainPage():

# @pytest.mark.open_page
# @pytest.mark.smoke
# def test_guest_can_go_to_catalogue(browser):
#  page = MainPage(browser, link)
#  page.open_page()
#  page.should_be_view_products()
#  page.go_to_catalogue()
#
# def test_guest_can_go_to_login_page(browser):
#  page = MainPage(browser, link)
#  page.open_page()
#  page.go_to_login_page()
#  time.sleep(2)
#  page = LoginPage(browser, link)
#  page.should_be_login_page()
#
# def test_user_should_be_autorized(browser):
#  link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#  page = LoginPage(browser, link)
#  page.open_page()
#  page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
#  page.should_be_autorized_user()
