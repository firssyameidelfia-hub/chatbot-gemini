import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Konfigurasi API Key Gemini agar terbaca dengan benar di Vercel
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

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
        # Menggunakan struktur pemanggilan Gemini versi stabil
       model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_text)
        
        # Pastikan dikembalikan dalam bentuk teks string murni untuk Flask
        return str(response.text)
    except Exception as e:
        return f"Waduh, ada kendala koneksi ke Gemini: {str(e)}"

# Ini penting agar Vercel bisa mengenali aplikasimu saat di-deploy
app = app
