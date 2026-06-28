import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Ambil setingan dari file .env
load_dotenv()

# 2. Siapkan koneksi ke Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. Minta Gemini buat jawab pertanyaan
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content('Halo Gemini! Saya sedang belajar membuat chatbot.')

# 4. Tampilkan jawabannya di terminal
print(response.text)
