import pytest
from selenium import webdriver
import allure
import uuid


@pytest.fixture()
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    if not request :
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            for log in browser.get_log('browser'):
                print(log)
        except:
            pass 

    print("\nquit browser..")
    browser.quit()