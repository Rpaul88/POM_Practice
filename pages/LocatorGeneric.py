

class LocatorGeneric():                                             #### 15 ####

    def __init__(self,driver):
        self.driver=driver

    def locator(self,loc_type,loc_val):

        if loc_type == 'id':
            ele = self.driver.find_element_by_id(loc_val)

        elif loc_type == 'xpath':
            ele = self.driver.find_element_by_xpath(loc_val)

        return ele



# Control ->Webgeneric.py                                         ##### 16 ####