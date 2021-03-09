from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():ß
    return "Hello Luckyjames : Happy New Years road to 2022-3000s"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)