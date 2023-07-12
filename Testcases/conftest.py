import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()