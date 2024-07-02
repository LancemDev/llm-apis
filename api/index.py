from flask import Flask, request, jsonify, render_template, redirect, make_response
from flask_cors import CORS
from openai import OpenAI
import openai
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


@app.route('/policy', methods=['POST'])
def policy():
    # Early exit if no data processing activities are provided
    data = request.get_json()
    data_processing_activities = data.get('dataProcessingActivities', [])
    if not data_processing_activities:
        return jsonify({"error": "No data processing activities provided"}), 400

    # Prepare the system message
    system_message = f"You are a helpful AI that generates privacy policies. The company performs the following data processing activities: {', '.join(data_processing_activities)}."

    # Make the API call to generate the privacy policy
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": "Generate a privacy policy for my company."}
        ]
    )
    

    response = completion.choices[0].message.content

    # Efficiently remove the last 19 words from the response
    response_words = response.split()
    if len(response_words) > 19:
        response = ' '.join(response_words[:-19])

    return jsonify({"response": response})


@app.route('/fitness', methods=['POST'])
def fitness():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fitness assistant, skilled in providing workout routines and nutrition advice."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})



@app.route('/gdpr-assistant', methods=['POST'])
def gdpr_assistant():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a GDPR assistant, skilled in providing information about GDPR compliance."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/agrik-chat', methods=['POST'])
def agrik_chat():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in providing information about agriculture and farming."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/transit-track', methods=['POST'])
def transit_track():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in helping users with navigation using our system transittrack, or help our drivers and sacco admins on questions regarding their areaa of work and our system that gives them solutions around vehicle monitoring and management.."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/')
def index():
  return "Hello, if you're not Lance, you're prolly lost"

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

@app.route('/landing', methods=['GET'])
def landing():
  return render_template('landing.html')

@app.route('/update-account', methods=['GET'])
def update_account():
  return render_template('update-account.html')

@app.route('/logout', methods=['GET'])
def logout():
  response = make_response(redirect('/login'))
  response.set_cookie('email', '', expires=0) 
  return response

@app.route('/contacts', methods=['GET'])
def contact():
  return render_template('contact.html')

@app.route('/training', methods=['GET'])
def training():
  return render_template('training.html')

@app.route('/buttons', methods=['GET'])
def buttons():
  return render_template('buttons.html')


if __name__ == '__main__':
  app.run(debug=True)