from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Wait:
    def __init__(self):
        pass

    def wait_by_visibility_of_element_located(self, driver, element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.visibility_of_element_located(element))
            return element
        except:
            return None

    def wait_by_visibility_all(self, driver, element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.visibility_of_all_elements_located(element))
            return element
        except:
            return None

    def wait_by_invisibility_of_element_located(self, driver, element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.invisibility_of_element_located(element))
            return element
        except:
            return None

    def wait_by_clickable(self, driver, element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.element_to_be_clickable(element))
            return element
        except:
            return None

    def wait_by_presence_of_all(self, driver, element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.presence_of_all_elements_located(element))
            return element
        except:
            return None

    def wait_by_title_is(self, driver, condition, time):
        try:
            element = WebDriverWait(driver, time).until(ec.title_is(condition))
            return element
        except:
            return None

    def wait_by_presence(self, driver, name_element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.presence_of_element_located(name_element))
            return element
        except:
            return None

    def wait_by_visibility_of(self, driver, name_element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.visibility_of(name_element))
            return element
        except:
            return None

    def wait_by_visibility_any(self, driver, name_element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.visibility_of_any_elements_located(name_element))
            return element
        except:
            return None

    def wait_by_invisibility_of_element(self, driver, name_element, time):
        try:
            element = WebDriverWait(driver, time).until(ec.invisibility_of_element(name_element))
            return element
        except:
            return None

    def wait_alert_is_present(self, driver, time):
        try:
            element = WebDriverWait(driver, time).until(ec.alert_is_present())
            return element
        except:
            return None

    def wait_by_title_contains(self, driver, condition, time):
        try:
            element = WebDriverWait(driver, time).until(ec.title_contains(condition))
            return element
        except:
            return None
