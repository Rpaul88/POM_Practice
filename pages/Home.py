# from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.WebGeneric import WebGeneric                                                        #### 10 ###

class Logout(WebGeneric):                    # Passed WebGeneric class as parameter            ### 11 ####

    def __init__(self,driver):     # Created a constructor>>to take driver ref from test file  #### 7 ####
        self.driver=driver
        WebGeneric.__init__(self,driver)     # Declared Webgeneric constructor inside driver   #### 12 ####
        self.logout_xpath="//a[text()='Log Out']"  # Declared locator values                   #### 13 ####

    def logout_cms(self):          # Need to change driver-->self.driver                       #### 8 ####

        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath("//img[@class='avatar avatar-26 photo']"))
        act.perform()
        self.driver.implicitly_wait(30)

        # self.driver.find_element_by_xpath("//a[text()='Log Out']").click()
        w = WebGeneric(self.driver)                                                            #### 14/15 ####
        w.submit1(self.logout_xpath)

