from locators.locators import LocatorsXPath
import pytest


class ContactUs:
    def __init__(self, driver):
        self.driver = driver
        self.name = LocatorsXPath.name
        self.email = LocatorsXPath.email
        self.telephone = LocatorsXPath.telephone
        self.country = LocatorsXPath.country
        self.company = LocatorsXPath.company
        self.message = LocatorsXPath.message
        self.submit = LocatorsXPath.submit
        self.clear = LocatorsXPath.clear

    def input_name(self):
        pass

    def input_email(self):
        pass

    def input_telephone(self):
        pass

    def input_country(self):
        pass

    def input_company(self):
        pass

    def input_message(self):
        pass

    def submit(self):
        pass
