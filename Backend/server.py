from datetime import date, datetime
from flask import Flask, request, url_for, send_file, make_response
from utils import get_word, get_image, translation, to_speech
import uuid
from flask_cors import CORS
from database import create_connection, create_table

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "*"}}, origins='*', supports_credentials=True)

users = dict()
images = dict()


@app.route("/image/")
def image():    
    uuid_val = request.cookies.get("uuid")
    if uuid_val is None:
        uuid_val = str(uuid.uuid4())
        uuid_val = uuid_val.replace("-", "")
        images[uuid_val] = get_image()
    print("uuid_val: ", uuid_val)
    prev_words = users.get(uuid_val, [])
    
    word = get_word()[0]

    while word in prev_words:
        word = get_word()[0]
    
    prev_words.append(word)

    if len(prev_words) % 10 == 0:
        prev_img = images[uuid_val]
        img = get_image()
        while prev_img != img:
            img = get_image()
        images[uuid_val] = img
    users[uuid_val] = prev_words
    
    to_speech(word=word, save_to="static/audio/", filename=word)

    img_path = "images/" + images[uuid_val]
    audio_path = "./audio/" + word + ".mp3"
    img_desc = "This image depicts the majestic Quebec \
                City skyline this is a long version of a \
                description hopefully this works"
    

    
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