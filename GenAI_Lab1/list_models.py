import google.generativeai as genai
import os
from dotenv import load_dotenv
#import google.genai as genai
from rich import print

load_dotenv()  # ← automatically finds .env in current or parent folder

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#print(dir(genai))
genai.configure(api_key= GOOGLE_API_KEY)


try:
    models = list(genai.list_models())
    print(f"✅ Key valid! {len(models)} models available.")
    for m in models:
        print(" -", m.name)
except Exception as e:
    print("❌ Invalid key:", e)