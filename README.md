
# Multi-Purpose Flask API

A Flask-based REST API that provides various AI-powered services using OpenAI's GPT-3.5-turbo model. The API includes endpoints for video recommendations, content rewriting, privacy policy generation, fitness advice, GDPR compliance, agricultural insights, childcare information, mental health support, and transit system assistance.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)

## Features
- Multiple specialized AI assistants for different domains
- CORS support for cross-origin requests
- Environment variable configuration
- Basic web interface with login functionality
- Session management using cookies

## Prerequisites
- Python 3.x
- Flask
- OpenAI API key
- python-dotenv
- flask-cors

## Installation
1. Clone the repository
2. Install required packages:
```bash
pip install flask flask-cors openai python-dotenv
```

## Environment Setup
1. Create a `.env` file in the root directory
2. Add your OpenAI API key:
```
api_key=your_openai_api_key_here
```

## API Endpoints

### AI Assistant Endpoints

#### 1. Video Recommendations
```
POST /message
```
Provides video recommendations and relevant information based on user queries.

#### 2. Content Rewriting
```
POST /gregorian-sarcasm
```
Rewrites text in a modern, Gen-Z style with witty and whimsical elements.

#### 3. Privacy Policy Generation
```
POST /policy
```
Generates custom privacy policies based on provided data processing activities.

#### 4. Fitness Assistant
```
POST /fitness
```
Provides workout routines and nutrition advice.

#### 5. GDPR Assistant
```
POST /gdpr-assistant
```
Offers guidance on GDPR compliance.

#### 6. Agricultural Assistant
```
POST /agrik-chat
```
Provides information about agriculture and farming.

#### 7. Childcare Assistant
```
POST /kindy-care-chat
```
Offers guidance on childcare and early childhood education.

#### 8. Mental Health Support
```
POST /mental-health
```
Provides mental health support and resources.

#### 9. Transit System Assistant
```
POST /transit-track
```
Helps users with navigation and vehicle monitoring systems.

#### 10. Agricultural Guard
```
POST /agri-guard
```
Provides specialized agricultural advice and insights.

### Web Interface Endpoints

#### Authentication
```
GET, POST /login
GET /logout
```

#### Pages
```
GET /
GET /maps
GET /homepage
GET /landing
GET /update-account
GET /contacts
GET /training
GET /buttons
```

## Authentication
The web interface implements basic authentication:
- Default credentials: 
  - Email: admin@gmail.com
  - Password: admin
- Session management using cookies
- Protected routes require authentication

## Usage Examples

### Making an API Request
```python
import requests
import json

# Example: Getting fitness advice
url = "http://localhost:5000/fitness"
payload = {
    "message": "I need a workout routine for beginners"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### Generating a Privacy Policy
```python
import requests
import json

url = "http://localhost:5000/policy"
payload = {
    "dataProcessingActivities": [
        "email collection",
        "user analytics",
        "payment processing"
    ]
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

## Development
To run the application in development mode:
```bash
python index.py
```
The application will start on `http://localhost:5000` with debug mode enabled.

## Security Considerations
- The application uses environment variables for sensitive data
- Basic authentication is implemented for web interface
- CORS is enabled for API access
- It's recommended to implement proper API authentication for production use

## Error Handling
- The API returns appropriate HTTP status codes
- JSON error responses include descriptive messages
- Invalid login attempts return 401 status code

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License.