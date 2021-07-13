import pytest
from selenium import webdriver

from TestData.DataToTest import Testdatainput


def pytest_addoption(parser):
    parser.addoption("--browser_name", action = "store", default = "chrome")
    parser.addoption("--channel_name", action = "store", default = "prod")

@pytest.fixture(scope="class")
def setup(request):
    browsername= request.config.getoption("browser_name")
    channelname= request.config.getoption("channel_name")

    if browsername== "chrome":
        driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        if channelname == "ete":
            driver.get("https://www.google.com")
        elif channelname == "prod":
            driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        if channelname == "cut":
            driver.get("https://www.google.com")
        elif channelname == "prod":
            driver.get("https://rahulshettyacademy.com/angularpractice/")
        elif channelname == "cut":
            driver.get("https://rahulshettyacademy.com/angularpractice/")

    if request.cls is not None:
        request.cls.driver = driver

    yield
    driver.quit()

@pytest.fixture(params= Testdatainput.testdatainputexcel("test_form"))
def formdata(request):
    return request.param

@pytest.fixture(params= Testdatainput.testdatainputexcel("test_shop"))
def shopdata(request):
    return request.param