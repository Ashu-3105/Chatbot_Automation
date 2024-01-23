from selenium import webdriver
import time
class infow():
    def __init__(self):
        self.driver=webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button')
        time.sleep(5)
        enter.click()
        time.sleep(20)




# assist = infow()
# assist.get_info("neutron star")