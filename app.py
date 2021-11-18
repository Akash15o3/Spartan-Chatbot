from flask import Flask, render_template, request, jsonify

from chat import get_response
from VGG_Net_For_Main_Page import Find_the_Main_Page
from Yolo5_For_GUI_Elements import DetectYOLO
app = Flask(__name__)


@app.get("/")
def index_get():

    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.post("/predictimage")
def predictimage():
    text = request.get_json().get("message")
    response = DetectYOLO(text)
    response2 = Find_the_Main_Page(text)
    result = response2 + response
    message = {"answer": result}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)