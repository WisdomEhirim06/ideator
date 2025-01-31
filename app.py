from flask import Flask, render_template, Response, url_for, jsonify
import os, requests
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__, template_folder='static/templates')

load_dotenv()


# Initialize model

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = 'https://openrouter.ai/api/v1/chat/completions'



CATEGORY_PROMPTS = {
    "startup_ideas": """Generate an innovative and unique startup idea.
Requirements:
- Should solve a real problem
- Be technically feasible
- Have a clear target market
- Have a straight idea response, no need to sound or greet someone
- Act as a startup founder or expert giving adivce to a startup enthusisat
- Provide brief one or two sentence description
- Must cut across different fields uniquely and to different regions
- Solves a problem that is not already solved
- Be creative and unexpected|3.00

Format your response to be a concise and compelling startup idea without sounding like an AI response""",
    
    "weekend_plans": """Create an unconventional and exciting weekend activity.
Requirements:
- Should be doable within 48 hours
- Should suit different personality types and preferences
- Be engaging and memorable
- Should sound human-generated
- Include specific details
- Weekend days include Friday, Saturday or Sunday be very specific
- Should be specific to Nigerians and must be have a mix of pidgin and english in the response
- Act like a 40-year-old Nigerin respponding to a 20-year-old Nigerian on how to enjoy the weekend
- Should be a mix of outdoor and indoor activities
- Just be natural and humanly relatable
- Have a straight idea response, no need to sound or greet someone
- Be social and engaging
- Break from typical routines

Format your response as a detailed and engaging weekend plan""",
    
    "writing_prompts": """Craft a thought-provoking writing prompt.
Requirements:
- Should spark creativity
- Should be usable by both beginners and experienced writers
- Should be relatable to all kind of writers not just fictional writers
- Include unique elements
- Should be short, 1-2 sentences
- Be open to interpretation
- Have a straight idea response, no need to sound or greet someone
- Challenge conventional thinking

Format your response as a well-crafted writing prompt""",
    
    "random_challenges": """Develop a fun personal challenge.
Requirements:
- Should be achievable
- Push comfort zones
- Should be short and brief.
- Should be specific to young Africans wiithin the range of 18-30
- Should involve relating to other people and learning new things
- Response should sound human-generated
- Be measurable
- Have a straight idea response, no need to sound or greet someone
- Create memorable experiences

Format your response as a fun and engaing personal challenge""",
    
    "creative_projects": """Invent an imaginative creative project.
Requirements:
- Should combine unexpected elements
- Have clear steps
- Should be brief with 1-2 sentences
- Must appeal to a broad audience and different fields
- Should be humanly relatable
- Be engaging
- Have a straight idea response, no need to sound or greet someone
- Result in a tangible output

Format your response as a fun and engaging creative project"""
}

def generate_with_openrouter(prompt):
    try:
        # OpenRouter request payload
        payload = {
            "model": "mistralai/mistral-7b-instruct:free",  # Free tier model
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a creative idea generator. Generate innovative and specific ideas tailored to the given category and requirements."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "max_tokens": 150,
            "temperature": 0.9,
            "top_p": 1.0
        }

        # Headers for OpenRouter API
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",  # Optional but recommended
            "X-Title": "Ideator App"  # Optional app name
        }

        # Make API call
        response = requests.post(
            OPENROUTER_BASE_URL, 
            json=payload, 
            headers=headers
        )

        # Check for successful response
        response.raise_for_status()
        
        # Extract idea from response
        response_data = response.json()
        idea = response_data['choices'][0]['message']['content'].strip()
        return idea
    
    except Exception as e:
        app.logger.error(f"OpenRouter API Error: {str(e)}")
        return f"Error generating idea: {str(e)}"

@app.route('/generate/<category>')
def generate_idea(category):
    if category not in CATEGORY_PROMPTS:
        return jsonify({"error": "Category not found"}), 404
    
    try:
        idea = generate_with_openrouter(CATEGORY_PROMPTS[category])
        return jsonify({"idea": idea})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

# Additional error handling and logging
@app.errorhandler(500)
def handle_500(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
