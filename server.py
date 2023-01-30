from flask import *
from dotenv import load_dotenv
import os

load_dotenv()
my_id = os.getenv("ID")


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html',user=user_name)