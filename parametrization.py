import pytest
import math
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, num):
    link = f"https://stepik.org/lesson/236{num}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    field_for_answer = browser.find_element_by_css_selector(".textarea")
    field_for_answer.click()
    field_for_answer.send_keys(answer)

    send = browser.find_element_by_css_selector('.submit-submission')
    send.click()
    field = browser.find_element_by_css_selector('.smart-hints__hint')

    print(field.text)

    assert field.text == "Correct!", "DOESN'T MATCH!!!"

