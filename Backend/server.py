from datetime import date, datetime
from flask import Flask, request, url_for, send_file, make_response
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "*"}})
 
@app.route("/")
def index():
    return "Index!"


@app.route("/register/")
def register():
    res = make_response()
    res.set_cookie("name", value="I am cookie")
    
    return res


@app.route("/image/")
def image():
    date_arg = request.args.get('date')
    if date_arg is None:
        date_arg = date.today()
    else:
        date_arg = datetime.strptime(date_arg, "%m/%d/%Y")
    
    print(date_arg)

    img_path = "./images/quebec_small.jpg"
    img_desc = "This image depicts the majestic Quebec City skyline"
    
    response = make_response(url_for('static', filename=img_path))

    # response.headers["Description"] = img_desc

    return "/static/quebec_small.jpg"


@app.route("/word/")
def word():
    date_arg = request.args.get('date')
    if date_arg is None:
        date_arg = date.today()
    else:
        date_arg = datetime.strptime(date_arg, "%m/%d/%Y")
    
    print(date_arg)

    word = "Bonjour mon cheri"

    return word

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)