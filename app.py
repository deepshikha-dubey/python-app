from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def home():
    return "My To-Do App is running in Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

logging.basicConfig(level=logging.INFO) 
logging.info("App started")
