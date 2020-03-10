from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! \n"

@application.route("/ready")
def ready():
    return "I am ready! \n"

@application.route("/health")
def health():
    return "I am Healthy! \n"

if __name__ == "__main__":
    application.run()
