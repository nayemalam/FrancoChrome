from datetime import date, datetime
from flask import Flask, request, send_file
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "*"}})
 
@app.route("/")
def index():
    return "Index!"


@app.route("/image/")
def image():
    date_arg = request.args.get('date')
    if date_arg is None:
        date_arg = date.today()
    else:
        date_arg = datetime.strptime(date_arg, "%m/%d/%Y")
    
    print(date_arg)
    
    return send_file("./images/quebec_small.jpg", mimetype="image/jpg")

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)