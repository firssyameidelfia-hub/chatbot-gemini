import os
from google import genai
from dotenv import load_dotenv

# 1. Ambil setingan dari file .env
load_dotenv()

# 2. Siapkan koneksi ke Gemini
client = genai.Client()

# 3. Minta Gemini buat jawab pertanyaan
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Halo Gemini! Saya sedang belajar membuat chatbot.',
)

# 4. Tampilkan jawabannya di terminal
print(response.text)