import requests
from pathlib import Path
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

# Example URL for engineering category
full_url_example = base_url + engineering

# Headers for HTTP requests
# Headers for HTTP requests
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=1D8E43C16A80AAF0F80AC401E24CF43B',
    'Host': 'ir.mksu.ac.ke',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://ir.mksu.ac.ke",
    "Referer": "http://ir.mksu.ac.ke/handle/123456780/219/",
    "Upgrade-Insecure-Requests": "1",
}

# Function to fill and submit the form for a single document
def submit_document(file):
    """
    Submits a document by filling and submitting the form.

    Args:
        file (FileStorage): The file to submit.

    Returns:
        dict: A JSON response indicating the status of the submission.
    """
    # Form data for the document
    form_data = {
        'dv_contributor_author_last': 'Machakos University',
        'dc_date_issued_year': '2022',
        'dc_date_issued_month': 'December',  # Assuming the date format is YYYY-MM
        'dv_publisher': 'Machakos University Press',
        'dc_type': 'Learning Object',
        'description': 'Past Examination Paper',
        'decision': 'accept',
        'dc_langauge': 'en', 
    }

    # Get title of the doc from the uploaded file
    form_data['dc_title'] = file.filename.split('.')[0]
    form_data['file'] = (file.filename, file.read())

    # Submit the form
    try:
        response = session.post(full_url_example + 'submit', data=form_data, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        print(f"Timeout occurred while submitting document '{file.filename}'")
        return None

    # Check if the submission was successful
    if response.status_code == 200:
        # print out the values submitted
        print(f"Title: {form_data['dc_title']}")
        print(f"Author: {form_data['dv_contributor_author_last']}")
        print(f"Year: {form_data['dc_date_issued_year']}")
        print(f"Month: {form_data['dc_date_issued_month']}")
        print(f"Publisher: {form_data['dv_publisher']}")
        print(f"Type: {form_data['dc_type']}")
        # print(f"License: {form_data['dv_license']}")
        print(f"Decision: {form_data['decision']}")
        print(f"Description: {form_data['description']}")
        print(f"File: {file.filename}")
        print(f"Document '{file.filename}' submitted successfully!")
    else:
        print(f"Failed to submit document '{file.filename}'. Status code: {response.status_code}")

    return response

# Route for testing
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

@app.route('/x', methods=['GET'])
def x():
    """
    A route for testing.

    Returns:
        str: The rendered template for the main page.
    """
    return render_template('main.html')

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

    response = session.post(login_url, data=login_data, headers=headers)
    if not response.ok:
        return "Login failed.....\nEmail: " + email + "\nPassword: " + password
    # Redirect to /test-uploads
    headers['Cookie'] = f'JSESSIONID={response.cookies["JSESSIONID"]}'
    return "Login successful!.....\nEmail: " + email + "\nPassword: " + password

@app.route('/fetch_html')
def fetch_html():
    """
    Fetches all the HTML from the base URL.

    Returns:
        str: The HTML of the base URL.
    """
    try:
        # Fetch cookies
        headers['Cookie'] = f'JSESSIONID={session.cookies["JSESSIONID"]}'
        response = requests.get(full_url_example, headers=headers)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"

    return response.text
    

if __name__ == "__main__":
    app.run(debug=True)
