from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
from flask import *
from selenium.webdriver.support.ui import Select
# Initialize the Chrome driver
driver = webdriver.Chrome()
keyboard = Controller()

app = Flask(__name__)

@app.route('/submit')
def submit_document():
    # Set the implicit wait time to 10 seconds. This means that Selenium will wait up to 10 seconds for elements to appear before throwing an exception
    driver.implicitly_wait(10)

    # Navigate to the login page
    driver.get('http://ir.mksu.ac.ke/password-login')

    # Find the email input field by its name and type in the email
    driver.find_element(By.NAME, 'login_email').send_keys('titutoo@mksu.ac.ke')

    # Find the password input field by its name and type in the password
    driver.find_element(By.NAME, 'login_password').send_keys('Kimarutitoy')

    # Simulate pressing the Return key to submit the form
    driver.find_element(By.NAME, 'login_password').send_keys(Key.RETURN)

    # Wait for 5 seconds to allow the page to load
    time.sleep(5)

    # Navigate to the submission page
    driver.get('http://ir.mksu.ac.ke/handle/123456780/219/submit')

    # Find the file input field by its name and type in the file path
    driver.find_element(By.NAME, 'file').send_keys('/uploads/1.pdf')

    # Find the author input field by its name and type in the author
    driver.find_element(By.NAME, 'dc_contributor_author_last').send_keys('Machakos University')

    # Find the title input field by its name and type in the title
    driver.find_element(By.NAME, 'dc_title').send_keys('1 test(to be deleted)')

    # Find the year input field by its name and type in the year
    driver.find_element(By.NAME, 'dc_date_issued_year').send_keys('2022')

    # Find the month dropdown list by its name
    month_dropdown = Select(driver.find_element(By.NAME, 'dc_date_issued_month'))

    # Select the desired option by visible text
    month_dropdown.select_by_visible_text('December')

    # Find the publisher input field by its name and type in the publisher
    driver.find_element(By.NAME, 'dc_publisher').send_keys('Machakos University Press')

    # Find the type dropdown list by its name
    type_dropdown = Select(driver.find_element(By.NAME, 'dc_type'))

    # Select the desired option by visible text
    type_dropdown.select_by_visible_text('Learning Object')

    # Select the desired language by its ISO code from the dropdown list
    language_dropdown = Select(driver.find_element(By.NAME, 'dc_language'))
    language_dropdown.select_by_value('en')

    # then click the next button to go to the other input fields
    driver.find_element(By.NAME, 'submit_next').click()

    # then click next again because the input fields in this page are not required
    driver.find_element(By.NAME, 'submit_next').click()

    # then choose the file from the choose file button
    driver.find_element(By.NAME, 'file').send_keys('C:\\Users\\User\\Desktop\\1.pdf')

    # Find the description input field by its name and type in the description
    driver.find_element(By.NAME, 'description').send_keys('Past Examination Paper')

    # Then click next to go to the next page
    driver.find_element(By.NAME, 'submit_next').click()

    # then click next again because the input fields in this page are not required
    driver.find_element(By.NAME, 'submit_next').click()

    # then click the checkbox to agree to grant the license
    driver.find_element(By.NAME, 'decision').click()

    # then click the complete submission button to submit the document
    driver.find_element(By.NAME, 'submit_next').click()

    # Wait for 5 seconds to allow the page to load
    time.sleep(5)

    # Print a success message
    print('Document submitted successfully!')

    return 'Document submitted successfully!'

@app.route('/test')
def test():
    return "Urls should be working!"

if __name__ == '__main__':
    app.run(debug=True)


