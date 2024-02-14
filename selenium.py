from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from flask import Flask, render_template, request, jsonify

# Create the Flask app
app = Flask(__name__)

# Base URL for the website
base_url = 'http://ir.mksu.ac.ke/handle/123456780/'

# Constants for different categories
agriculture = "189/"
business = "217/"
education = "218/"
engineering = "219/"
environment = "221/"
health_sciences = "220/"
hospitality = "216/"
humanities = "188/"
pure_sciences = "215/"

# Example URL for the engineering category
full_url_example = base_url + engineering

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode to avoid opening a window

def submit_document(file):
    # Set up the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Form data for the document
    form_data = {
        'dv_contributor_author_last': 'Machakos University',
        'dc_date_issued_year': '2022',
        'dc_date_issued_month': 'December',  # Assuming the date format is YYYY-MM
        'dv_publisher': 'Machakos University Press',
        'dc_type': 'Learning Object',
        'dc_langauge': 'en',
        'description': 'Past Examination Paper',
        'decision': 'on',
    }

    # Get title of the doc from the uploaded file
    form_data['dc_title'] = file.filename.split('.')[0]
    form_data['file'] = file.filename

    # URL to submit the form
    target_url = 'http://ir.mksu.ac.ke/handle/123456780/219/submit'
    login_url = 'http://ir.mksu.ac.ke/password-login'
    credentials = {
        'email': 'titutoo@mksu.ac.ke',
        'password': 'Kimarutitoy',
    }

    try:
        # Navigate to the login page
        driver.get(login_url)

        # Fill in the login form
        email_input = driver.find_element(By.NAME, 'login_email')
        password_input = driver.find_element(By.NAME, 'login_password')
        email_input.send_keys(credentials['email'])
        password_input.send_keys(credentials['password'])
        password_input.send_keys(Keys.RETURN)

        # Wait for the login to complete
        WebDriverWait(driver, 10).until(EC.url_contains('/password-login'))

        # Navigate to the submission page
        driver.get(target_url)

        # Fill in the submission form
        for key, value in form_data.items():
            input_element = driver.find_element(By.NAME, key)
            input_element.send_keys(value)

        # Upload the file
        file_input = driver.find_element(By.NAME, 'file')
        file_input.send_keys(file.filename)

        # Submit the form
        submit_button = driver.find_element(By.NAME, 'submit')
        submit_button.click()

        print(f"Document '{file.filename}' submitted successfully!")
    except Exception as e:
        print(f"Error submitting document '{file.filename}': {e}")
    finally:
        # Close the browser
        driver.quit()

    return response

@app.route('/test')
def test():
    """
    A test route to check if the URLs are working.

    Returns:
        str: A test message indicating that the URLs are working.
    """
    return "Urls should be working!"

@app.route('/test-uploads')
def test_uploads():
    """
    A route to test file uploads.

    Returns:
        str: The rendered template for the file upload page.
    """
    return render_template('/home/index.html')

@app.route('/')
def index():
    """
    The main route of the application.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Machakos University IR API!"

def save_doc(file):
    """
    Saves a document to the uploads directory.

    Args:
        file (FileStorage): The file to save.
    """
    upload_dir = Path('uploads')
    upload_path = upload_dir / file.filename
    
    # Create the directory if it doesn't exist
    try:
        upload_dir.mkdir(parents=True)
    except FileExistsError:
        pass
    
    file.save(upload_path)
    print(f"File {file.filename} saved successfully.")

@app.route('/submit_documents', methods=['POST'])
def submit_documents():
    """
    Submits multiple documents.

    Returns:
        str: A message indicating the status of the file processing.
    """
    uploaded_files = request.files.getlist('documents')

    # Process the uploaded files as needed
    for i, file in enumerate(uploaded_files, start=1):
        try:
            print(f"Processing file {i} of {len(uploaded_files)}: {file.filename}")

            # Save each file
            # print(f"Saving file {file.filename}...")
            # save_doc(file)
            # print(f"File {file.filename} saved.")

            # Then submit the document
            print(f"Submitting file {file.filename}...")
            submit_document(file)
            print(f"File {file.filename} submitted.")
        except Exception as e:
            print(f"Error processing file {file.filename}: {e}")

    print("All files processed.")
    return 'Files processed'

@app.route('/login', methods=['GET'])
def login_get():
    """
    A route to display the login page.

    Returns:
        str: The rendered template for the login page.
    """
    return render_template('home/login.html')

session = requests.Session()

@app.route('/login', methods=['POST'])
def login_post():
    """
    Handles the login form submission.

    Returns:
        str: A message indicating the status of the login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    password_input_name = "login_password"
    email_input_name = "login_email"

    login_url = base_url + "password-login"

    login_data = {
        email_input_name: email,
        password_input_name: password
    }

    response = session.post(login_url, data=login_data)
    if not response.ok:
        return "Login failed.....\nEmail: " + email + "\nPassword: " + password
    # Redirect to /test-uploads
    headers['Cookie'] = f'JSESSIONID={response.cookies["JSESSIONID"]}'
    return "Login successful!.....\nEmail: " + email + "\nPassword: " + password


@app.route('/fetch-sth')
def fetch_sth():
    """
    Logs in and fetches something from the base URL.

    Returns:
        str: The response from the base URL.
    """
    login_url = 'http://ir.mksu.ac.ke/password-login'
    target_url = 'http://ir.mksu.ac.ke/handle/123456780/221/submit'
    credentials = {
        'login_email': 'titutoo@mksu.ac.ke',
        'login_password': 'Kimarutitoy',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'amp_6e403e=y7amtQ0LsgPgK8SnXM3eGG...1hearcqsl.1hearcqsl.0.0.0; _ga=GA1.1.100642076.1700651316; _ga_NF2FGF1NDQ=GS1.1.1700651315.1.1.1700651468.60.0.0; JSESSIONID=1D8E43C16A80AAF0F80AC401E24CF43B',
        'Host': 'ir.mksu.ac.ke',
        'Referer': 'http://ir.mksu.ac.ke/handle/123456780/187',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    with requests.Session() as session:
        post = session.post(login_url, data=credentials, headers=headers)
        response = session.get(target_url, headers=headers)

    return response.text


if __name__ == "__main__":
    app.run(debug=True)
