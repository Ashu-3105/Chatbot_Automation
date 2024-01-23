from selenium import webdriver
class music():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def play(self,query):
        self.query=query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element("xpath",'//*[@id="dismissable"]')
        video.click()




# assist = music()
# assist.play('Arijit singh song')
