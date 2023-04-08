#Test_locators.py


class login_locators:
    username_input_box = 'username' # Name
    password_input_box = 'password' # Name
    submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' #Xpath

class pimpage_locators:
    pim_click = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a' # Xpath
    addemployee_click = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a' # Xpath
    firstname_input_box = 'firstName' # Name
    lastname_input_box = 'lastName' # Name
    Save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'#Xpath
    
class pimpageedit_locators:
    Employee_List_click = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a' # Xpath
    employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input' #Xpath
    search_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]' #Xpath
    edit_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]' #Xpath
    lastname_inputbox = 'lastName' # Name
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button' # Xpath
    delete_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i' # Xpath
    suredelete_button ='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]' # Xpath


