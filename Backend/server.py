from datetime import date, datetime
from flask import Flask, jsonify, Request, request, url_for, send_file, make_response
from utils import get_word, get_image, translation, to_speech
import uuid
from flask_cors import CORS
import json
from database import create_connection, create_table

app = Flask(__name__)
CORS(app, supports_credentials=True, 
resources={"/*": {"origins": "*"}},
expose_headers=["img_description", "word", "translation", "audio_file"])

users = dict()
images = dict()


@app.route("/image/")
def image():    
    uuid_val = request.cookies.get("uuid")

    print("UUID Cookie: ", uuid_val)
    # If the user has never been authenticated
    if(uuid_val is None or 
        uuid_val not in images):
        # Assign user a uuid value
        uuid_val = str(uuid.uuid4())
        uuid_val = uuid_val.replace("-", "")

        # Get image and description pair
        images[uuid_val] = get_image()
    print("uuid_val: ", uuid_val)

    # Get a list of all prev words user has seen or empty list if none
    prev_words = users.get(uuid_val, [])
    

    word = get_word()[0]
    while word in prev_words:
        word = get_word()[0]
    
    prev_words.append(word)

    # Get prev img and desc for the user
    img_list = images[uuid_val]

    print("Prev words: ", prev_words)
    print("len(prev_words): ", len(prev_words))
    # Change image after 10 words
    if len(prev_words) % 10 == 0:
        print("Entered if")
        prev_img = images[uuid_val][0]
        img_list = get_image()
        print("img_list: ", img_list)
        print("prev_img: ", prev_img)
        # import pdb; pdb.set_trace()
        while prev_img == img_list[0]:
            img_list = get_image()
        images[uuid_val] = img_list
    users[uuid_val] = prev_words
    img_list = images[uuid_val]
    to_speech(word=word, save_to="static/audio/", filename=word)

    img_path = "images/" + img_list[0]
    audio_path = "./audio/" + word + ".mp3"
    img_desc = img_list[1]
    
    print("Description: ", img_list[1])

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
    # , host='0.0.0.0'
    app.run(debug=True, port=8080, threaded=True)