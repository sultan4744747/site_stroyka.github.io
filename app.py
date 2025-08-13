

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

TOKEN = "8282618951:AAGgk1nbykAyWjmdTX5f210MjLb3zqkqOew"
CHAT_ID = "2016140316"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    text = f"📩 Новая заявка\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": text}
    resp = requests.post(url, params)

    if resp.status_code == 200:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(debug=True)