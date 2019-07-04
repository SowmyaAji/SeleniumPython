
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
# driver.get("https://github.com")
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("ogmaciel")
# elem.send_keys(Keys.RETURN)
# next = driver.find_element_by_partial_link_text("ogmaciel")
# next.click()


class HomePageTest:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.github.com"
        self.verificationErrors = []

    def test_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        assert "GitHub" in driver.title

    # run a function to return the results of the search bar in Github for the word "Python"
    def test_search_repo(self):
        elem = self.driver.find_element_by_name("q")
        assert elem is not None
        elem.clear()
        elem.send_keys("Python")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    # run a function to find the repositories of an individual and click open the individual's home page
    def test_search_indv(self):
        elem = self.driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys("ogmaciel")
        elem.send_keys(Keys.RETURN)
        next = self. driver.find_element_by_partial_link_text("ogmaciel")
        next.click()

# check whether the login button on the github home page logs the person into their repository
