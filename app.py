import os
from flask import Flask, render_template, request, jsonify, redirect
app = Flask(__name__)

# 환경변수에서 PORT 값을 가져오고, 없으면 기본값 5000을 사용함.
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/pricing.html')
def pricing():
    return render_template('pricing.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)  # 여기서 포트를 설정합니다.