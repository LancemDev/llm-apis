from flask import Flask, request, jsonify, render_template, redirect, make_response
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.getenv('api_key'))

@app.route('/message', methods=['POST'])
def get_message():
  data = request.get_json()
  user_message = data.get('message')

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an AI assistant, skilled in recommending videos and providing relevant information about them."},
      {"role": "user", "content": user_message}
    ]
  )

  # Modify the response handling to provide video recommendations and relevant information
  response = completion.choices[0].message.content

  return jsonify({"response": response})

@app.route('/gregorian-sarcasm', methods=['POST'])
def gregorian_sarcasm():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in rewriting, NOT REPLYING, the text in a modern, gen-z, witty, and whimsical manner."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/')
def index():
  return "Go to route /message to get a response from the AI model."

@app.route('/maps')
def maps():
  return render_template('maps.html')

@app.route('/login', methods=['GET'])
def login():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
  data = request.form
  email = data.get('email')
  password = data.get('password')

  if email == 'admin@gmail.com' and password == 'admin':
    response = make_response(redirect('/homepage'))
    response.set_cookie('email', email)  # Set the email cookie
    return response
  
  # Add a return statement to handle the case when the email and password do not match
  return "Invalid email or password", 401

@app.route('/homepage')
def homepage():
  if not request.cookies.get('email'):
    return redirect('/login')
  return render_template('homepage.html')

if __name__ == '__main__':
  app.run(debug=True)