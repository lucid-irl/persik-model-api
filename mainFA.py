from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from class_text_preprocess import predictSVM, predictLC

app = FastAPI()

class Article(BaseModel):
    article_id: int
    title: str
    content: str
    category: str
    is_anonymous: Optional[bool] = None
    
@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/article")
def get_Article(article: Article):
    return {"article_id": article.article_id, "Category": article.category}

@app.put("/predict")
def predict_Article(article: Article):
    articleContent = article.content
    # svm = predictSVM(articleContent)
    # lc = predictLC(articleContent)
    article.category = '1 + lc'
    return {"article_id": article.article_id, "Category": article.category}