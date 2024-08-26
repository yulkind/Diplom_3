from urllib import request

import pytest
from selenium import webdriver


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Unknown browser: {request.param}')
    yield driver
    driver.quit()
