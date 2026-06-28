import os
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_text,
    )
    
    return response.text

if __name__ == "__main__":
    app.run(debug=True)

else:
    # Ini penting agar Vercel bisa mengenali aplikasimu saat di-deploy
    app = app