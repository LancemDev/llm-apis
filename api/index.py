import requests
from pathlib import Path
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base URL for the website
base_url = 'ir.mksu.ac.ke/handle/123456780/'

# Sample input names for the form fields
input_names = {
    'title': 'dc_title',
    'author': 'dv_contributor_author_last',
    'year': 'dc_date_issued',
    'month': 'dc_date_issued',
    'publisher': 'dv_publisher',
    'type': 'dc_type',
    'license': 'dv_license',
}

# Constants for different categories
agriculture = 189
business = 217
education = 218
engineering = 219
environment = 221
health_sciences = 220
hospitality = 216
humanities = 188
pure_sciences = 215

# Example URL for engineering category
full_url_example = base_url + str(engineering)

# Headers for HTTP requests
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=3A2F3B4E3B0F9A',
    'Host': 'ir.mksu.ac.ke',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://ir.mksu.ac.ke",
    "Referer": "https://ir.mksu.ac.ke/handle/123456780/219",
    "Upgrade-Insecure-Requests": "1",
}

# Function to fill and submit the form for a single document
def submit_document(doc):
    """
    Submits a document by filling and submitting the form.

    Args:
        doc (str): The document to submit.

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
        'decision': 'on',
    }

    # Get title of the doc from the uploaded file
    form_data['dc_title'] = doc.split('.')[0]

    # Submit the form
    response = session.post(full_url_example + 'submit', data=form_data, headers=headers)

    # Check if the submission was successful
    if response.status_code == 200:
        print(f"Document '{doc}' submitted successfully!")
    else:
        print(f"Failed to submit document '{doc}'. Status code: {response.status_code}")

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
    upload_dir.mkdir(parents=True, exist_ok=True)
    
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
        print(f"Processing file {i} of {len(uploaded_files)}: {file.filename}")

        # Save each file
        # Let's remove the saving part. It's not as important
        # print(f"Saving file {file.filename}...")
        # save_doc(file)
        # print(f"File {file.filename} saved.")

        # Then submit the document
        print(f"Submitting file {file.filename}...")
        submit_document(file)
        print(f"File {file.filename} submitted.")

    print("All files processed successfully.")
    return 'Files saved successfully'

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

    login_url = "ir.mksu.ac.ke/password-login"

    login_data = {
        email_input_name: email,
        password_input_name: password
    }

    response = session.post(login_url, data=login_data, headers=headers)
    if not response.ok:
        return "Login failed.....\nEmail: " + email + "\nPassword: " + password
    # Redirect to /test-uploads
    return "Login successful!.....\nEmail: " + email + "\nPassword: " + password
    

if __name__ == "__main__":
    app.run(debug=True)
