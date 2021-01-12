from flask import Flask
server = Flask(__name__)

def hello():
    return "Hello from Luckyjames"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)