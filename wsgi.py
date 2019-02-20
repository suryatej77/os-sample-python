from flask import Flask
application = Flask(__name__)

@application.route("/")
def homepage():
	return render_template('homepage.html')

if __name__ == "__main__":
    application.run()
