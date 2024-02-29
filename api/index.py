from flask import Flask, request, jsonify
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
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": user_message}
    ]
  )

  return jsonify({"response": completion.choices[0].message.content})  # Access the content attribute

@app.route('/')
def index():
  return "We are live my bwoy"

if __name__ == '__main__':
  app.run(debug=True)