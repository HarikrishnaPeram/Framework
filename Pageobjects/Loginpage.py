
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_css = "button[type='submit']"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver
    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id ).send_keys("admin@yourstore.com")
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys("admin")
    def clickLogin(self,login):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_css).click()
    def clickLogout(self,logout):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()