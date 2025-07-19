from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read WELCOME_MESSAGE from .env (with fallback)
message = os.getenv("WELCOME_MESSAGE", "Hello from fallback!")

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>{message}</h1>"
