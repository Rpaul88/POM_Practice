from pages.Login import Login
from pages.Home import Logout
from data.TestData import *
import pytest                          # added after introducing conftest.py                 #### 2 #####

@pytest.mark.usefixtures("test_setup") # Applying fixture to every test methods in the class #### 4 #####
                                       # test_setup-->conftest method name
class Test_cms:                                                                              #### 3 #####
                                       # After introducing conftest.py, Both methods defined under the class---Test_cms

    def test_login(self):              # Passed self as parameter, after declaring under class
        driver=self.driver             # Accessing web driver instance with self.driver      #### 5 #####
        lp=Login(driver)               # Need to pass driver inside Login()
        lp.login_cms(USERNAME,PASSWORD)

    def test_logout(self):
        driver=self.driver             # Accessing web driver instance with self.driver      #### 6 #####
        lp=Logout(driver)              # Need to pass driver inside Logout()
        lp.logout_cms()

# Need to pass driver reference to pages class object creation                                ##### 7 #####
