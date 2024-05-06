import pytest
from selenium import webdriver


@pytest.fixture
def chrome(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()