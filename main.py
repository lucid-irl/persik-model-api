from flask import Flask
from flask import request

from class_text_preprocess import remove_stopwords, text_preprocess

app = Flask(__name__)

@app.route("/")
def hi():
    return "hi"

@app.route("/predict")
def predict():
    doucument = "asdasdadegywehtewfef"
    doucument = remove_stopwords(doucument)
    doucument = text_preprocess(doucument)
    return doucument

if __name__ == "__main__":
    app.run()