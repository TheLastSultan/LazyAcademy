from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
import time
import smtplib


# Download and install chromedriver, then link the path into this variable
# CHROME_DRIVER_ADDRESS
chromedriver = "/home/mobro/Desktop/pythonwebdriver/chromedriver"

# change this for automatic texts
PHONE_NUMBER_OR_EMAIL=" YOURPHONENUMBER@txt.att.net"
    # use a phone number or email above
    # if you are using verizion it's YOURPHONENUMBER@vtext.com
    # if you are using tmobile it's  YOURPHONENUMBER@@tmomail.net
YOUR_GITHUB_USERNAME = "TheLastSultan"
YOUR_GITHUB_PASS = "YOURPASS"




gmail_user = "YOUREMAIL@email.com"
gmail_password = "YOURPASSWORD@email.com"

def send_alert_email(subject, body, to=[]):
    """
    subject: string
    body: string
    return boolean
    """

    from_mail = gmail_user
    to = ['EXAMPLEEMAIL@EMAIL.COM']

    email_text = """From: %s
To: %s
Subject: %s

%s""" % (from_mail, ', '.join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_mail, to, email_text)
    server.close()

def send_successful_text():
    send_alert_email("Login attempt Successful!'", "We be alright out here", to=[PHONE_NUMBER_OR_EMAIL] )

def send_unsuccessful_text():
    send_alert_email("Login attempt FAILED", "Don't forget to log in yourself", to=[PHONE_NUMBER_OR_EMAIL])

driver = webdriver.Chrome(chromedriver)

# Github login

# Don't change the sleep times. If it runs too fast it will set off site alarms
def login():
    time.sleep(1)
    WebDriverWait(driver,10)

    # Navigate to website
    driver.get("https://progress.appacademy.io/me/sign_in")

    # Find sign in
    driver.find_element_by_partial_link_text('Sign in with').click()
    time.sleep(1)

    # Enter your username and password
    driver.find_element_by_id('login_field').send_keys("YOURUSERNAME")
    driver.find_element_by_id('password').send_keys("YOURPASS")
    driver.find_element_by_name('commit').click()
    time.sleep(1)

    # You are logged in, let's click the form
    driver.find_element_by_class_name('student-check-in-form').click()



try:
    login()
except NoSuchElementException:
    send_unsuccessful_text()
else:
    send_successful_text()
    



# There is occasionally an authentication page

# Headless options
# need to download chrome cnry
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(chrome_options = chrome_options)
