# Import Modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json,os

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


# Open Chrome Browser
options = Options()
options.add_experimental_option("detach", True )
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



post_content = "https://xtralapz.com/top-5-lipstick-shades-for-every-skin-tone/"
# post_content = "HELL0ooooo"

post_content = str(post_content)



def saveCookies(driver):
    # Get and store cookies after login
    cookies = driver.get_cookies()

    # Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')


def loadCookies():
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

        # Load cookies to a vaiable from a file
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        # Set stored cookies to maintain the session
        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')
    
    driver.refresh() # Refresh Browser after login


def fb_login():
    loginURL = 'https://facebook.com/'
    driver.get(loginURL)
    
    username = driver.find_element(By.CLASS_NAME,"inputtext")
    passward = driver.find_element(By.ID,"pass")

    login_button = driver.find_element(By.NAME,"login")
    # u_0_5_M7
    # login
    username.send_keys("username")
    passward.send_keys("passward")

    time.sleep(1)
    login_button.click()


# Check if cookies file exists
cookies_file = 'cookies.json'
cookies_exist = os.path.exists(cookies_file)


print('In the end******************************')
# Example: go to Facebook homepage
# driver.get('https://facebook.com/')
driver.get('https://web.facebook.com/groups/767293308836501')

# If cookies exist, load them; otherwise, login
if cookies_exist:
    print('Loading cookies*************************')
    loadCookies()
else:
    # Open Facebook login page
    fb_login()
    print('Saving cookies***************')
    saveCookies(driver)

# Close the browser
# driver.quit()

time.sleep(1)


print('is about to post#####################')


# # home opening
# home = driver.find_element(By.XPATH,"//a[contains(@class,'x1i10hfl xjbqb8w')]")
# home.click()
# time.sleep(1)
# whats on your mind cliking

your_mind= driver.find_element(By.XPATH,"//span[text()='Write something...']")
your_mind.click()
time.sleep(2)

# writing_post = driver.find_element(By.XPATH, "(//div[@contenteditable='true']//p)[2]")
writing_post = driver.find_element(By.XPATH, "//div[@class='_1mf _1mj']")
time.sleep(2)
writing_post.send_keys(post_content)
time.sleep(5)


post_button = driver.find_element(By.XPATH,"//span[text()='Post']")
post_button.click()

