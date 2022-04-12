from flask import Flask
from flask import request
from flask import jsonify
import json

from class_text_preprocess import callmodel

app = Flask(__name__)


@app.route("/")
def hi():
    return "hi"

article = {}

@app.route("/getArticle", methods=['POST'])
def get_article():
    doucument = json.loads(request.data)
    article["des"] = doucument
    print(doucument)
    # escapes = ''.join([chr(char) for char in range(1, 32)])
    # t = doucument.translate(None, escapes)

    
    return json.dumps(doucument, ensure_ascii=False).encode('utf8')

@app.route("/predict")
def predict_article():
    
    
    
    doc = article["des"]
    lable = callmodel(doc)
    return lable

languages =[]
@app.route("/languages", methods=['POST'])
def create_language():
    body = json.loads(request.data)
    languages.append(body)
    return jsonify(body)

@app.route("/languages")
def get_languages():
  return jsonify(languages)

if __name__ == "__main__":
    app.run()