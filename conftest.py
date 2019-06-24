import pytest                                #### 1 #####

@pytest.fixture(scope='class') # Fixtures-->used to teardown the code
                               # To create fixtures-->@pytest.fixture
                               # scope="class"--->perform an action before and after of an class of a module


def test_setup(request):       # test_setup-->conftest method name/fixture name

    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Framework1/drivers/chromedriver.exe")
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")
    driver.implicitly_wait(30)
    request.cls.driver=driver

# Control ->test_loginout.py                 ##### 2 #####


# Fixtures help us to setup some pre-conditions that should run before any tests are executed.

