from flask import Flask, jsonify, request 
from werkzeug.serving import WSGIRequestHandler
import face_recognition
import base64
import random
import os
# creating a Flask app 
app = Flask(__name__) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/v1/image/face_recognition', methods = ['POST']) 
def home(): 
    data=request.files
    if data!=None:
        image_1 = face_recognition.load_image_file( data['file1'])
        face_encoding_1 = face_recognition.face_encodings(image_1)
        image_2 = face_recognition.load_image_file( data['file2'])
        face_encoding_2 = face_recognition.face_encodings(image_2)
        if len(face_encoding_2)==0:
            return "No_Face_Detected"
        elif len(face_encoding_2)>1:
            return "More_Than_One_Face"
        else:
            results = face_recognition.face_distance([face_encoding_1[0]], face_encoding_2[0])
            print(results)
            return str(results[0])
    else:
        return "", 404

    
@app.route('/v1/image/face_detection', methods = ['POST','GET']) 
def yuip(): 
    data=request.files
    if data!=None:
        image = face_recognition.load_image_file( data['file'])
        face_encoding = face_recognition.face_encodings(image)
        
        return str(len(face_encoding))
    else:
        return "", 404





@app.route("/")
def index():
    
    return "<h1>Hello, World</h1>"

if __name__ == "__main__":
    # https://stackoverflow.com/questions/63765727/unhandled-exception-connection-closed-while-receiving-data
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded=True, host='0.0.0.0', port=5000)