import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# UBAH BARIS INI: Tambahkan api_version='v1' di dalamnya
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"), api_version='v1')
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
        # Memanggil model Gemini 1.5 Flash
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_text)
        return str(response.text)
    except Exception as e:
        return f"Waduh, ada kendala koneksi ke Gemini: {str(e)}"

app = app
