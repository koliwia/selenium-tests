import pytest
from selenium import webdriver
from utilities.test_data import TestData

@pytest.fixture(params=["chrome"])
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.sign_up_url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()
