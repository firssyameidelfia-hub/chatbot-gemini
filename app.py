import os
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Inisialisasi client Google GenAI dengan memaksa versi API 'v1' agar tidak lari ke v1beta
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options={'api_version': 'v1'}
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    
    if not user_text:
        return "Maaf, pesan tidak boleh kosong."
        
    try:
        # Menggunakan struktur pemanggilan SDK terbaru yang stabil
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=user_text
        )
        return str(response.text)
    except Exception as e:
        return f"Waduh, ada kendala koneksi ke Gemini: {str(e)}"

# Ini penting agar Vercel bisa mengenali aplikasimu saat di-deploy
app = apps
