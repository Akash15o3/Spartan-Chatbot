import os

from flask import Flask, render_template, request, jsonify

from chat import get_response, get_questions
from VGG_Net_For_Main_Page import Find_the_Main_Page
from Yolo5_For_GUI_Elements import DetectYOLO, DetectYOLOTestCaseGroup
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
    text = request.get_json().get("image")
    text2 = request.get_json().get("message")
    print(text , text2)
    response2 = Find_the_Main_Page(text)
    response3 =''
    x = ''
    y = ''
    z = ''
    response4 = ""
    if (response2 == 'Looks like you are in Data_Administration_With_Graph Tab. '):
        response = DetectYOLO(text,text2)
        # x = "On this tab, following are the functionalities : "
        # for r in response:
        #     x = x + r + " , "
        # response3 = get_questions("Data_Administration_With_Graph")
        response4 = get_response(text2)
        # y = "You can ask me following questions. "
        # count = 1
        # for r in response3:
        #     y = '\n'+ y + f"{count}. {r}" + " "
        #     count+=1
        abc = sorted(os.listdir('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/'))
        print(abc)
        z = abc[len(abc) - 1]
        print("IMAADSd",z)
        print(response3)

    elif (response2 == 'Looks like you are in Test_Case_Group Tab. '):
        response = DetectYOLOTestCaseGroup(text, text2)
        # x = "On this tab, following are the functionalities : "
        # for r in response:
        #     x = x + r + " , "
        # response3 = get_questions("Test_Case_Group")
        response4 = get_response(text2)
        # y = "You can ask me following questions. "
        # count = 1
        # for r in response3:
        #     y = '\n' + y + f"{count}. {r}" + " "
        #     count += 1
        abc = sorted(os.listdir('/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/static/bounding_images/'))
        print(abc)
        z = abc[len(abc)-1]
        print("img to be sent",z)
        print(response3)

    elif (response2 == 'Looks like you are in Input_Image_Modulation Tab. '):
        response3 = get_questions("Input_Image_Modulation")
        y = "You can ask me following questions. "
        count = 1
        for r in response3:
            y = '\n' + y + f"{count}. {r}" + " "
            count += 1
        print(response3)

    elif (response2 == 'Looks like you are in Main_Page Tab. '):
        response3 = get_questions("Main_Page")
        y = "You can ask me following questions. "
        count = 1
        for r in response3:
            y = '\n' + y + f"{count}. {r}" + " "
            count += 1
        print(response3)

    elif (response2 == 'Looks like you are in Contact Tab. '):
        response3 = get_questions("Contact")
        y = "You can ask me following questions. "
        count = 1
        for r in response3:
            y = '\n' + y + f"{count}. {r}" + " "
            count += 1
        print(response3)

    elif (response2 == 'Looks like you are in Data_Administration Tab. '):
        response3 = get_questions("Data_Administration")
        y = "You can ask me following questions. "
        count = 1
        for r in response3:
            y = '\n' + y + f"{count}. {r}" + " "
            count += 1
        print(response3)

    else:
        response = ""


    result = z+ response4 + x + y
    message = {"answer": result}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)