from flask import Flask, render_template, request, redirect
from scraper import *
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        URL = request.form.get("Url")
        budget = (float)(request.form.get("budget_"))
        toemail = request.form.get("mail_")
        check_price(URL, budget, toemail)
    return render_template('index.html')


if (__name__ == "__main__"):
    app.run(port=5000, debug=True)
