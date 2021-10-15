# from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium import webdriver


class Base:
    def __init__(self):
        path = 'driver/chromedriver.exe'
        self.driver = webdriver.Chrome(path)

    @pytest.fixture()
    def set_up(self):
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.seleniumframework.com/Practiceform/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
