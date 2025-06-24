from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/show')
def show_data_from_app1():
    try:
        # Replace this with your actual deployed App 1 URL
        response = requests.get("https://flash-app-deploy-on-render2.onrender.com/data")
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}

    return jsonify({"received_data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)