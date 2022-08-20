from flask import Flask

app = Flask(__name__)

@app.route("/" , methods=['GET' , 'POST'])
def faceDetection():
    return "Works"

if __name__ == "__main__" :
    app.run(debug= True, host='127.0.0.1',port=8000)