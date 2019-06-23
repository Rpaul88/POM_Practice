from pages.WebGeneric import WebGeneric                                                      #### 10 ###

# driver configuration shifted to conftest.py      ## Moved to conftest.py                   #### 1 ####
# driver=webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Framework1/drivers/chromedriver.exe")
# driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

class Login(WebGeneric):                     # Passed WebGeneric class as parameter          ### 11 ####


    def __init__(self,driver):   # Created a constructor>>to take driver ref from test file  #### 7 ####
        self.driver=driver
        WebGeneric.__init__(self,driver)     # Declared Webgeneric constructor inside driver  #### 12 ####
        self.un_id="user_login"              # Declared locator values                        #### 13 ####
        self.pwd_id="user_pass"
        self.sb_id="wp-submit"

    def login_cms(self,UN,PWD):  # Need to change driver-->self.driver                       #### 8 ####

        # self.driver.find_element_by_id("user_login").send_keys(UN)
        # self.driver.find_element_by_id("user_pass").send_keys(PWD)
        # self.driver.find_element_by_id("wp-submit").click()

        w=WebGeneric(self.driver)            #### 14 ####
        w.enter(self.un_id,UN)
        w.enter(self.pwd_id,PWD)
        w.submit(self.sb_id)







# Control ->Webgeneric.py                                                                    ##### 9 ####

# Control-->LocatorGeneric.py                                                                #### 15 ####