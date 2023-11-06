
# using flask_restful 
from flask import Flask, jsonify, request 
import flask
from flask_restful import Resource, Api 
from angle_calculator import angle_calc
from ellipse_generator import ellipse_gen
from line_generator import line_gen
import base64
from flask_cors import CORS




# creating the flask app 
app = Flask(__name__) 
# creating an API object 
# api = Api(app)
CORS(app)

@app.route('/')
def hello_world():
    return flask.send_from_directory('','index.html')
  
@app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True) 
    threshold = input_json['threshold']
    photo_data = base64.b64decode(input_json['photo'])

    with open("image.jpg", "wb") as file:
        file.write(photo_data)

    c = line_gen("image.jpg")

    h,k,a,b = ellipse_gen("image.jpg","Line_image.jpg",c,threshold)


    angle1,angle2 = angle_calc(a,b,c,h,k)
    
    encoded_string = ""
    with open("Ellipse_fitted_on_image.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    data = {
        "angle1" : angle1,
        "angle2" : angle2,
        "result" : "{}".format(encoded_string.decode('utf-8'))
    }

    response = jsonify(data) 
   
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True)
