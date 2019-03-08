from flask import Flask
from flask import render_template
from os import chdir, listdir

app = Flask(__name__)

@app.route("/")
def videos():
	arquivos = listdir('.\static')
	mp4 = []
	for a in arquivos:
		if a.endswith(".mp4"):
			mp4.append(a)
	return render_template('home.html', filmes=mp4)

if __name__ == "__main__":
	app.run(debug=True)
