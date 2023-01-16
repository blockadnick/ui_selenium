from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


css = By.CSS_SELECTOR
xpth = By.XPATH
id = By.ID

class BasePage:

    url = "https://www.sitexample.com"


    def __init__(self, driver):
        self.driver = driver

    def open(self, link):
        self.driver.get(link)

    def accept_cookie(self):
        self.click((css, ".button-accept-cookie"))

    def zoom(self, percent):  
        return self.driver.execute_script(f"document.body.style.zoom='{percent}%'")

    def find(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()   

    def click_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def presence_click(self, by_locator, time):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(by_locator)).click()

    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def clear_by_keys(self, element):
        self.send_keys((element), Keys.CONTROL + 'a')
        self.send_keys((element), Keys.BACKSPACE)

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(by_locator))
        return element.text

    def disappear(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(by_locator))

    def is_title(self, title):
        WebDriverWait(self.driver, 3).until(EC.title_is(title))
        return self.driver.title

    def is_url_contains(self, url_part):
        element = WebDriverWait(self.driver, 3).until(EC.url_contains(url_part))
        return bool(element)

    def is_correct_page(self, url_part):
        try:
            self.is_url_contains(url_part)
            return True
        except:
            return False

    def element_ready(self, element, time):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
            return True
        except:
            return False

    def element_presence(self, element, time):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(element))
            return True
        except:
            return False

    def scroll_to(self, element):
        target_element = self.find(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target_element)

    def scroll_on_height(self, height):
        self.driver.execute_script(f"window.scrollTo(0,{height})")

    def move_to_point(self, x, y):
        ActionChains(self.driver).move_by_offset(x, y).context_click().perform()

    def hover_to_element(self, element):
        target_element = self.find(element)
        ActionChains(self.driver).move_to_element(target_element).perform()

    def hover_click(self, element):
        target_element = self.find(element)
        ActionChains(self.driver).move_to_element(target_element).click(target_element).perform()

    def hover_doubleclick(self, element):
        target_element = self.find(element)
        ActionChains(self.driver).move_to_element(target_element).double_click(target_element).perform()

    def jump_from_input(self, element):
        self.send_keys(element, Keys.DOWN)
        self.send_keys(element, Keys.TAB)

    def change_country(self, country):
        self.click((css, ".country-name > span"))
        self.click((css, f".webui-popover-content li[data-country='{country}']"))



        