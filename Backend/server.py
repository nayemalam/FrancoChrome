from datetime import date, datetime
from flask import Flask, request, url_for, send_file, make_response
from word import get_word, translation, to_speech
import uuid
from flask_cors import CORS
from database import create_connection, create_table

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "*"}})

users = dict()

 
@app.route("/")
def index():
    return "Index!"


@app.route("/image/")
def image():    
    uuid_val = request.cookies.get("uuid")
    if uuid_val is None:
        uuid_val = str(uuid.uuid4())
        uuid_val = uuid_val.replace("-", "")
    print("uuid_val: ", uuid_val)
    prev_words = users.get(uuid_val, [])
    
    word = get_word()[0]

    while word in prev_words:
        word = get_word()[0]
    
    print(word)

    prev_words.append(word)

    users[uuid_val] = prev_words
    
    to_speech(word=word, save_to="static/audio/", filename=word)

    img_path = "./quebec_small.jpg"
    audio_path = "./static/audio/" + word + ".mp3"
    img_desc = "This image depicts the majestic Quebec City skyline"
    
    response = make_response(url_for('static', filename=img_path))

    response.headers["img_description"] = img_desc
    response.headers["word"] = word
    response.headers["translation"] = translation(word)["translatedText"]
    response.headers["audio_file"] = url_for('static', filename=audio_path)
    response.set_cookie("uuid", value=uuid_val)

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
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)