import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not user_text:
        return "Maaf, pesan tidak boleh kosong."
    if not api_key:
        return "Waduh, API Key Gemini belum dipasang di Vercel Settings."
        
    try:
        # Menggunakan HTTP Request langsung ke API resmi Gemini v1
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{
                "parts": [{"text": user_text}]
            }]
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        
        # Ambil teks jawaban dari respon Google
        bot_reply = response_data['candidates'][0]['content']['parts'][0]['text']
        return str(bot_reply)
        
    except Exception as e:
        return f"Waduh, ada kendala koneksi ke Gemini: {str(e)}"

app = app
