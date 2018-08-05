from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import getpass

'''
# Selenium program that will automatically pay my car payment if the bank can recognize the device. Currently the program
# allows the me to enter my username and password. In addition, I can specify how much money I want to pay.
'''

# Function that allows the page load and locate the element we need
def page_timeout(timeout, element):
    # Locate the pay button and if the button is not located then we time out
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, element))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")




# Initialize Chrome by creating an object and open the Bay Federal site
browser = webdriver.Chrome()
browser.get('https://www.bayfed.com/')

# Find the "Account Login" button and click on it
account_login_btn = browser.find_element_by_css_selector('#form1 > header > div.headerwrap.container > div > div > div.trigger > a')
account_login_btn.click()

# Find the username and password input boxes
username = browser.find_element_by_css_selector('#userid')
password = browser.find_element_by_css_selector('#password')

# getpass is used to hide the username and password while its being inputed into the console
get_username = getpass.getpass('Enter your username: ')
get_password = getpass.getpass('Enter your password: ')


# Fill in the username and password boxes with the users credentials that were entered
username.send_keys(get_username)
password.send_keys(get_password)

# Find the "Login Now" button and click on it
login_now = browser.find_element_by_css_selector('#form1 > header > div.headerwrap.container > div > div > div.form > div.links.clearfix > a')
login_now.click()

# While loop to allow the user to enter the security code so the program can continue to automate the payment
while (browser.current_url != 'https://www.bayfedonline.com/tob/live/usp-core/app/home'):
    #print('You have failed')

    # Once the current url is equal to the one we want allow the page to load
    if(browser.current_url == 'https://www.bayfedonline.com/tob/live/usp-core/app/home'):
        break
    
page_timeout(5, '#payButtonEAklYU1IQxI-pT7Kh_Cj6aDu80oai6ayoZwSih-89E0')
pay_now = browser.find_element_by_css_selector('#payButtonEAklYU1IQxI-pT7Kh_Cj6aDu80oai6ayoZwSih-89E0')
pay_now.click()


# Click on the amount input field
page_timeout(10, '#amountInputField')
amount = browser.find_element_by_css_selector('#amountInputField')
amount.click()


get_amount_to_pay = 402.28
amount.send_keys(get_amount_to_pay)

timeout = 15
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@title="Select account"]'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print(browser.current_url)
    print("Timed out waiting for page to load")

# Click on the "Select Account" button
select_account = browser.find_element_by_xpath('//*[@title="Select account"]')
select_account.click()

# Click "Membership savings" from the drop down menu
member_savings = browser.find_element_by_css_selector('#accountDropdownFrom > div > div:nth-child(1) > div.hidden-xs._3MuGuqnnxfskvbijWA34l5 > div > div > div > ul > li > span > div')
member_savings.click()

# Click the "Make Transfer" button
make_transfer = browser.find_element_by_css_selector('#makeTransfer')
make_transfer.click()

# Confirm the amount and pay
confirm = browser.find_element_by_css_selector('#transfersConfirmationConfirmButton')
confirm.click()




