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