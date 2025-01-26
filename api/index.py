from flask import Flask, request, jsonify, render_template, redirect, make_response
from flask_cors import CORS
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv('api_key')

@app.route('/message', methods=['POST'])
def get_message():
  data = request.get_json()
  user_message = data.get('message')

  completion = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an AI assistant, skilled in recommending videos and providing relevant information about them."},
      {"role": "user", "content": user_message}
    ],
    max_tokens=150,
    temperature=0.7,
    top_p=1,
    timeout=10
  )

  # Modify the response handling to provide video recommendations and relevant information
  response = completion.choices[0].message.content

  return jsonify({"response": response})

@app.route('/gregorian-sarcasm', methods=['POST'])
def gregorian_sarcasm():
    data = request.get_json()
    user_message = data.get('message')

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in rewriting, NOT REPLYING, the text in a modern, gen-z, witty, and whimsical manner."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        timeout=10
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
    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": "Generate a privacy policy for my company."}
        ],    
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        timeout=10
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

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fitness assistant, skilled in providing workout routines and nutrition advice."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        timeout=10
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})



@app.route('/gdpr-assistant', methods=['POST'])
def gdpr_assistant():
    data = request.get_json()
    user_message = data.get('message')

    completion = openai.Completion.create(
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

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in providing information about agriculture and farming."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        timeout=10
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})

@app.route('/kindy-care-chat', methods=['POST'])
def kindy_care_chat():
    data = request.get_json()
    user_message = data.get('message')

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in providing information about childcare and early childhood education."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/mental-health', methods=['POST'])
def mental_health():
    data = request.get_json()
    user_message = data.get('message')

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in providing mental health support and resources."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})


@app.route('/')
def index():
  return "Hello, if you're not Lance, you're prolly lost"

if __name__ == '__main__':
  app.run(debug=True)