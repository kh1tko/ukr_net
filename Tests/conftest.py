import pytest
from selenium import webdriver


# @pytest.fixture
# def chrome():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(2)
#     yield driver
#     driver.quit()


@pytest.fixture
def firefox(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    request.cls.driver = driver
    yield driver
    driver.quit()
