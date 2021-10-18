import flask
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request
from flask_cors import CORS, cross_origin
from tensorflow import keras
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

def translate(x):
    return {
        1: 'This papaya is medium!',
        2: 'This papaya is ripe!',
        3: 'This papaya is unripe!',
        4: 'error'
    }.get(x, 4)

@app.route('/api', methods=['GET'])
@cross_origin()
def test():
    return {'test' : 'success'}


# A route to return all of the available entries in our catalog.
@app.route('/api/predict', methods=['POST'])
@cross_origin()
def upload_file():
    # data = request.files['file'].stream.read()
    data = request.files['file']
    data.save('./static/papaya.png')
    result = predict()
    return {'payload' : result}


def predict():
    model = tf.keras.models.load_model('first-model.h5')
    result = []
    img = cv2.imread('./static/papaya.png')
    img = cv2.resize(img,(128,128))
    img = img / 255.
    img= img.reshape(128,128,3)
    result.append(img)
    result = np.array(result)
    classes = model.predict(result)
    # print(classes)
    classes = np.array(classes)
    status = ''
    if (np.argmax(classes)==1):
      status = 'This papaya is medium'
    elif (np.argmax(classes)==2):
      status = 'This papaya is ripe'
    else:
      status = 'This papaya is unripe'
    return { 'status': status }

# def predict():
#     model = tf.keras.models.load_model('first-model.h5')
#     img = image.load_img('./static/papaya.png', target_size=(128, 128))
#     # img = cv2.imread('./static/papaya.png')
#     img = cv2.resize(img,(128,128))
#     img = img / 255.
#     img = img.reshape(128,128,3)
#     # x = image.img_to_array(img)
#     # x = np.expand_dims(x, axis=0)
#     # images = np.vstack([x])
#     classes = model.predict(img)
#     print(classes)
#     # score = tf.nn.softmax(classes[0])
#     # cl = str (float(np.max(score))*100)[:5]
#     # return {'status' : translate(np.argmax(classes[0])), 'confident_level': cl}
#     return {'status' : translate(np.argmax(classes[0])), 'confident_level': cl}

app.run()