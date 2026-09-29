import os
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("AQ.Ab8RN6IBEuhojWl2NPaSmj1erUP7nvWCf7g4F35YSL_XYeQN-Q")

def get_home_recommendations(budget, room_type):
    current_key = os.getenv("GOOGLE_API_KEY") or api_key
    
    if not current_key:
        return "Error: GOOGLE_API_KEY is missing in your .env file."
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=current_key)
        
        # gemini-2.5-flash model for higher limit & fast response
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"Create a concise budget breakdown for a {room_type} interior within ₹{budget} INR. List key items with estimated prices and store suggestions (IKEA, Amazon, Flipkart)."
        
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            return "Quota Limit Hit: Too many requests in 1 minute. Please wait 15-20 seconds and click 'Generate Plan' again."
        return f"Gemini API Error: {error_msg}"