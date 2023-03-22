
import time
from selenium.webdriver.common.by import By

def test_add_busket_button(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    element = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert element, "Button isn't found"

if __name__ == "__main__":
    test_add_busket_button()
    print("All tests are finished!")