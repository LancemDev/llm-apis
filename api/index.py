import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base URL for the website
base_url = 'https://ir.mksu.ac.ke/handle/123456780/'

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

agriculture = 189
business = 217
education = 218
engineering = 219
environment = 221
health_sciences = 220
hospitality = 216
humanities = 188
pure_sciences = 215


full_url_example = base_url + str(engineering)

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
    return jsonify({'message': 'Document submitted!', 'status': 'success'})
    # Form data for the document
    form_data = {
        'dv_contributor_author_last': 'Machakos University',
        'dc_date_issued_year': '2022',
        'dc_date_issued_month': 'December',  # Assuming the date format is YYYY-MM
        'dv_publisher': 'Machakos University Press',
        'dc_type': 'Learning Object',
        'decision': 'on',
    }

    # form_data['additional_field'] = 'additional_value'
    # get title of the doc from the uploaded file
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
    return "Urls should be working!"

@app.route('/test-uploads')
def test_uploads():
    return render_template('home/index.html')

@app.route('/')
def index():
    return render_template('test/index.html')

def save_doc(file):
    upload_path = f'uploads/{file.filename}'
    
    if(file.save(upload_path)):
        return file.filename + " saved successfully"


    

@app.route('/submit_documents', methods=['POST'])
def submit_documents():
    uploaded_files = request.files.getlist('documents')

    # Process the uploaded files as needed
    for file in uploaded_files:
        # Save each file
        save_doc(file)
        # then submit the document
        submit_document(file)

    return 'Files saved successfully'

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('home/login.html')

session = requests.Session()

@app.route('/login', methods=['POST'])
def login_post():
    # return "Login successful!"
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
    # redirect to /test-uploads
    return "Login successful!.....\nEmail: " + email + "\nPassword: " + password
    

if __name__ == "__main__":
    app.run(debug=True)
