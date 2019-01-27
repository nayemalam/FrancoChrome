from datetime import date, datetime
from flask import Flask, request, url_for, send_file, make_response
from word.word import get_word, translation, to_speech
import io
from flask_cors import CORS
from database import create_connection, create_table

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

    
    cookie_data = request.cookies.get("name")
    print("Cookie_data: ", cookie_data)

    img_path = "./quebec_small.jpg"
    audio_path = "./output.mp3"
    img_desc = "This image depicts the majestic Quebec City skyline"
    
    response = make_response(url_for('static', filename=img_path))

    response.headers["img_description"] = img_desc
    response.headers["word"] = "Bonjour"
    response.headers["translation"] = "Hello"
    response.headers["audio_file"] = url_for('static', filename=audio_path)

    return response


@app.route("/word/")
def word():
    date_arg = request.args.get('date')
    if date_arg is None:
        date_arg = date.today()
    else:
        date_arg = datetime.strptime(date_arg, "%m/%d/%Y")
    
    print(date_arg)

    response = make_response("Bonjour")

    response.headers["Translation"] = "Hello"

    return response

 
if __name__ == "__main__":
    word = get_word()[0]
    print(word)
    print(translation(word))
    print(to_speech(word=word))
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)