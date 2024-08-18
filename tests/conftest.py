import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#@pytest.fixture(params=['Chrome', 'Firefox'])
#def driver(request):
#    if request.param == 'Chrome':
#       driver = webdriver.Chrome()
#   elif request.param == 'Firefox':
#       driver = webdriver.Firefox()
#   else:
#       raise ValueError(f'Unknown browser: {request.param}')
#   yield driver
#   driver.quit()

#@pytest.fixture
#def user():
#    response = create_user_api_handler(login, password)
#    yield login, password
#    delete_user_api_handler(response['user_id'])

