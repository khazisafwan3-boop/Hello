from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Instructions to run:
    # 1. Install Flask: pip install flask
    # 2. Run the app: python flask-hello-world.py
    # 3. Open http://127.0.0.1:5000 in your browser
    app.run(debug=True)