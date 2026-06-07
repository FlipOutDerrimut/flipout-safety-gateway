import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Compliance Gateway Active. Access via Deputy link."

@app.route('/safety')
def safety_video():
    # This is the verification code staff will enter into Deputy
    completion_code = "SAFE-7729" 
    return render_template('safety.html', code=completion_code)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
