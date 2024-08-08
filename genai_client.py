import google.generativeai as genai
from config import API_KEY

# Configure the generative model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_content(full_prompt):
    try:
        response = model.generate_content(full_prompt)
        return response.text if hasattr(response, 'text') else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"There was an error generating the response: {str(e)}"