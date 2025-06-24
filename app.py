from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Change this to the actual deployed URL of app2 on Render
        response = requests.get("https://google.com")
        api_response = response.json().get("message", "No response")
    except Exception as e:
        api_response = f"Error contacting API: {e}"

    return render_template("index.html", api_response=api_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)