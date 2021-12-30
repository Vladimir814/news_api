from app import app
from flask import render_template
from .utils import get_news


@app.route('/')
def hello():
    user = {'name': "Vladimir"}
    return render_template("index.html", user=user)


@app.route('/news')
def news_headlines():
    news_articles = get_news()
    return render_template('news.html', news_articles=news_articles)

