from flask import Flask # Web framework for Python
import psycopg2 # PostgreSQL database adapter for Python (client library)
import os # Access to environment variables

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # Try to connect to the PostgreSQL using env variables

        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        return "✅ Connected to PostgreSQL!"
    except Exception as e:
        # If connection fails, show error message
        return f"❌ PostgreSQL connection failed: {e}"
    
if __name__ == '__main__':
    # Start Flask app on 0.0.0.0:8080 so it's accesible from Docker
    app.run(host="0.0.0.0", port=8080)