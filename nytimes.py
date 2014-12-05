from flask import Flask, jsonify, render_template, url_for
import requests, json

NYTimes_API_KEY = 'ca470e1e91b15a82cc0d4350b08a3c0b:14:70189328'
app = Flask(__name__, static_folder='static', static_url_path='/static')

NYTimes_Search_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q={0}+&api-key=' + NYTimes_API_KEY

def searchArticle(topic):
	r = requests.get(NYTimes_Search_URL.format(topic))
	data = json.loads(r.text)
	return data['response']['docs']

@app.route("/")
def urlRoute():
	return render_template('index.html', article=searchArticle('Artificial Intelligence'))

if __name__ == "__main__":
	app.run()