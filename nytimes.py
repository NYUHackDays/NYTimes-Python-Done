from nytimesarticle import articleAPI
from flask import Flask, jsonify, render_template, url_for

NYTimes_API_KEY = 'ca470e1e91b15a82cc0d4350b08a3c0b:14:70189328'
app = Flask(__name__, static_folder='static', static_url_path='/static')

def getArticle():
	api = articleAPI(NYTimes_API_KEY)
	articles = api.search(q = 'Artificial Intelligence')
	return articles

@app.route("/")
def urlRoute():
	return render_template('index.html', article=getArticle())

if __name__ == "__main__":
	app.run()