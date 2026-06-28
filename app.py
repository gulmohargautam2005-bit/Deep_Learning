from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import os
from src.utils.common import decodeImage 
from src.pipeline.prediction import PredictionPipeline

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

client = ClientApp()

@app.route('/', methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, client.filename)
    prediction = client.classifier.predict()
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# Trigger comment for CI/CD pipeline run
