from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import login_data
from Test_Data.data import addemployee_data
from Test_Data.data import editemployee_data
from Test_Locators.locators import login_locators
from Test_Locators.locators import pimpage_locators
from Test_Locators.locators import pimpageedit_locators
import pytest

class Test_Gayu:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
       
    def test_valid_login(self, boot):
        self.driver.get(login_data().url)
        self.driver.implicitly_wait(30)
        # enter user name
        self.driver.find_element(by=By.NAME, value= login_locators().username_input_box).send_keys(login_data().username)
        # enter password
        self.driver.find_element(by=By.NAME, value= login_locators().password_input_box).send_keys(login_data().password)
        # click submit
        self.driver.find_element(by=By.XPATH, value= login_locators().submit_button).click()

        assert self.driver.title =='OrangeHRM'
        print(" SUCCESS : Logged in with the Username Admin & ****** " )

    
    def test_invalid_login(self, boot):
        self.driver.get(login_data().url)
        self.driver.implicitly_wait(30)
        # enter user name
        self.driver.find_element(by=By.NAME, value=login_locators().username_input_box).send_keys(login_data().username)
        # enter valid password
        self.driver.find_element(by=By.NAME, value=login_locators().password_input_box).send_keys("invalid_password")
        # click submit
        self.driver.find_element(by=By.XPATH, value= login_locators().submit_button).click()

        assert self.driver.title =='OrangeHRM'
        print("invalid credential : Logged in with the Username {a} & {b}")
  
    def test_addemployee(self, boot):
        self.driver.get(login_data().url)
        self.driver.implicitly_wait(30)
        # enter user name
        self.driver.find_element(by=By.NAME, value= login_locators().username_input_box).send_keys(login_data().username)
        # enter password
        self.driver.find_element(by=By.NAME, value= login_locators().password_input_box).send_keys(login_data().password)
        # click submit
        self.driver.find_element(by=By.XPATH, value= login_locators().submit_button).click()
        # go to PIM page
        self.driver.find_element(by=By.XPATH, value =pimpage_locators().pim_click).click()
        # go to add Employee
        self.driver.find_element(by=By.XPATH, value=pimpage_locators().addemployee_click).click()
        # enter the credentials
        self.driver.find_element(by=By.NAME, value=pimpage_locators().firstname_input_box).send_keys(addemployee_data().firstName)
        self.driver.find_element(by=By.NAME, value=pimpage_locators().lastname_input_box).send_keys(addemployee_data().lastName)
        #save the details 
        self.driver.find_element(by=By.XPATH, value=pimpage_locators().Save_button).click()
        
        assert self.driver.title =='OrangeHRM'
        print("Employee details added successfully")

   
   
    def test_edit_employee(self, boot):
        self.driver.get(login_data().url)
        self.driver.implicitly_wait(30)
        # enter user name
        self.driver.find_element(by=By.NAME, value= login_locators().username_input_box).send_keys(login_data().username)
        # enter password
        self.driver.find_element(by=By.NAME, value= login_locators().password_input_box).send_keys(login_data().password)
        # click submit
        self.driver.find_element(by=By.XPATH, value= login_locators().submit_button).click()
        # go to PIM page
        self.driver.find_element(by=By.XPATH, value =pimpage_locators().pim_click).click()
        # Go to Employee List page
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().Employee_List_click).click()
        # Search for employee
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators ().employee_name).send_keys(addemployee_data().firstName)
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().search_button).click()
        # Edit employee details
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().edit_button).click()
        self.driver.find_element(by=By.NAME, value= pimpageedit_locators().lastname_inputbox).send_keys(editemployee_data().lastname)
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().save_button).click()      
        
        assert self.driver.title =='OrangeHRM'
        print(" employee details edited successfully")


    def test_delete_employee(self, boot):
        self.driver.get(login_data().url)
        self.driver.implicitly_wait(30)
        # enter user name
        self.driver.find_element(by=By.NAME, value= login_locators().username_input_box).send_keys(login_data().username)
        # enter password
        self.driver.find_element(by=By.NAME, value= login_locators().password_input_box).send_keys(login_data().password)
        # click submit
        self.driver.find_element(by=By.XPATH, value= login_locators().submit_button).click()
        # go to PIM page
        self.driver.find_element(by=By.XPATH, value =pimpage_locators().pim_click).click()
        # Go to Employee List page
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().Employee_List_click).click()
        # Search for employee
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators ().employee_name).send_keys(addemployee_data().firstName)
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().search_button).click()
        # Delete employee
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().delete_button).click()
        self.driver.find_element(by=By.XPATH, value=pimpageedit_locators().suredelete_button).click()
       
        assert self.driver.title =='OrangeHRM'
        print(" employee details deleted successfully ")

