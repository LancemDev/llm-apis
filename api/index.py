from flask import Flask, request, jsonify, render_template
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
            {"role": "system", "content": "You are an AI assistant, skilled in rewriting the following text in an old-fashioned, witty and whimsical manner. Avoid archaic words like 'thou' and the like. Do not reply, just rewrite the text."},
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

if __name__ == '__main__':
  app.run(debug=True)