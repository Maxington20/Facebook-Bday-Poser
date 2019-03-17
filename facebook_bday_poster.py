from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

# Found this code online which makes it so that the popup asking
#  if I want to allow notifications will not popup
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

# page I want to visit
driver.get('http://www.facebook.com')

# find email input and input my email 
emailelement = driver.find_element_by_xpath('.//*[@id="email"]')
emailelement.send_keys(username)

# find password input and input my password
passwordfield = driver.find_element_by_xpath('.//*[@id="pass"]')
passwordfield.send_keys(password)

# Find login button and then click it
loginbutton = driver.find_element_by_xpath('.//*[@id="loginbutton"]')
loginbutton.click()
time.sleep(5)

driver.get('http://facebook.com/events/birthdays')

# Create an empty array to store first names in
names = []
full_names = []
bdays_wished = []
# Can add full names to this list of people you don't want to wish happy birthday to
bad_names = []

# todaysbdays = driver.find_element_by_class_name('_4-u3')
name_divs = driver.find_elements_by_class_name('_tzn')

for name in name_divs:
        elements = name.find_elements_by_tag_name('a')
        for element in elements:
                full_names.append(element.text)
                firstname = element.text.split(' ',1)[0]
                names.append(firstname)
                      
count = 0
bdayposts = driver.find_elements_by_tag_name('textarea')
for bday in bdayposts:   
        if 'birthday' in bday.get_attribute('title'):
                # May need to remove the line below. Not sure if it will work
                # if names[count] in :
                if full_names[count] in bad_names:
                        print('You did not want to wish ' + names[count] + ' a happy bday!')
                else:
                        time.sleep(5)
                        bday.send_keys('Happy Birthday ' + names[count] + ' ')
                        # commented the line below out to test before posting tomorrow
                        time.sleep(5)
                        bday.send_keys(Keys.RETURN)
                        bdays_wished.append(full_names[count])
                        time.sleep(5)
                count += 1

if (bdays_wished):
        print('You wished Happy Birthday(s) to: ' + str(bdays_wished))

else:
        print('There were either no birthday\'s today, or nobody you wanted to wish happy birthday to')
driver.quit()