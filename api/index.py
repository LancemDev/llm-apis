import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route('/submit')
def submit_document():
    # Start a session
    session = requests.Session()

    # Login
    login_payload = {
        'login_email': 'titutoo@mksu.ac.ke',
        'login_password': 'Kimarutitoy'
    }
    login_req = session.post('http://ir.mksu.ac.ke/password-login', data=login_payload)

    # Check if login was successful
    if login_req.status_code != 200:
        return 'Login failed!'

    # Submit document
    submit_payload = {
        'file': ('1.pdf', open('/uploads/1.pdf', 'rb')),
        'dc_contributor_author_last': 'Machakos University',
        'dc_title': '1 test(to be deleted)',
        'dc_date_issued_year': '2022',
        'dc_date_issued_month': 'December',
        'dc_publisher': 'Machakos University Press',
        'dc_type': 'Learning Object',
        'dc_language': 'en',
        'description': 'Past Examination Paper'
    }
    submit_req = session.post('http://ir.mksu.ac.ke/handle/123456780/219/submit', files=submit_payload)

    # Check if submission was successful
    if submit_req.status_code != 200:
        return 'Submission failed!'

    return 'Document submitted successfully!'

@app.route('/test')
def test():
    return "Urls should be working!"

if __name__ == '__main__':
    app.run(debug=True)