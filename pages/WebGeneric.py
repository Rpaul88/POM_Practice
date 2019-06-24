from pages.LocatorGeneric import LocatorGeneric                                           #### 17 ####

class WebGeneric(LocatorGeneric):

    def __init__(self,driver):   # Created a constructor>>to take driver ref from test file  #### 9 ####
        self.driver=driver
        LocatorGeneric.__init__(self, driver)                                             #### 18 ####

    # def enter(self,locator,input_val):
    def enter(self,loc_type,loc_val,inp_val):                                             #### 19 ####

        # self.driver.find_element_by_id(locator).send_keys(input_val)
        self.locator(loc_type,loc_val).send_keys(inp_val)                                 #### 20 ####

    # def submit(self,locator):
    def submit(self,loc_type,loc_val):

        # self.driver.find_element_by_id(locator).click()
        self.locator(loc_type,loc_val).click()

    # def submit1(self,locator):
    def submit1(self,loc_type,loc_val):

        # self.driver.find_element_by_xpath(locator).click()                 # for xpath       #### 15 ####
        self.locator(loc_type,loc_val).click()



