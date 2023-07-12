import pytest
from selenium import webdriver
from Pageobjects.Loginpage import Login
class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepageTitle(self, setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title= self.driver.title()
        self.driver.close()
        if act_title == "your store.login":
            assert True
        else:
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title()
        self.driver.close()
        if act_title=="nopCommerce administration":
            assert True
        else:
            assert False


