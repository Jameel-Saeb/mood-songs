from flask import Flask, render_template, request
from textblob import TextBlob
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

# TODO: Add all of the routes you want below this line!


@app.route("/")
def index():
	if request.method == 'GET':
    	return render_template("index.html")
	else:
		text = request.form['text']
		blob = TextBlob(text)

		lst = [i.sentiment.polarity for i in blob.sentences]
		result = round(sum(lst)/len(lst), 2)

		if result > 0.49: #super happy
			pass
		elif result < -0.49: #super sad
			pass
		elif result >= 0.1: #happy
			pass
		elif result <  -0.1: #sad
			pass
		else: #neutral
			pass


			


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)