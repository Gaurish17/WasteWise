from flask import Flask, request, render_template, redirect, jsonify
from flask_jsglue import JSGlue # this is use for url_for() working inside javascript which is help us to navigate the url
import util
import os
import warnings
warnings.filterwarnings('ignore')
from werkzeug.utils import secure_filename

application = Flask(__name__)

# JSGlue is use for url_for() working inside javascript which is help us to navigate the url
jsglue = JSGlue() # create a object of JsGlue
jsglue.init_app(application) # and assign the app as a init app to the instance of JsGlue

util.load_artifacts()
#home page
@application.route("/home",methods=["GET", "POST"])
def home():
    return render_template("home.html")

@application.route("/",methods=["GET", "POST"])
def index():
    return render_template("index.html")

@application.route("/fruit",methods=["GET", "POST"])
def fruit():
    return render_template("fruit.html")


@application.route('/chat', methods=["GET", "POST"])
def chat():
  return render_template('chat.html')


@application.route("/contact",methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@application.route("/tracker",methods=["GET", "POST"])
def tracker():
    return render_template("tracker.html")

@application.route("/pickup",methods=["GET", "POST"])
def pickup():
    return render_template("pickup.html")
@application.route("/maps",methods=["GET", "POST"])
def maps():
    return render_template("maps.html")


#classify waste
@application.route("/classifywaste", methods = ["POST"])
def classifywaste():
    image_data = request.files["file"]
    #save the image to upload
    basepath = os.path.dirname(__file__)
    image_path = os.path.join(basepath, "uploads", secure_filename(image_data.filename))
    image_data.save(image_path)

    predicted_value, details, video1, video2 = util.classify_waste(image_path)
    os.remove(image_path)
    return jsonify(predicted_value=predicted_value, details=details, video1=video1, video2=video2)

# here is route of 404 means page not found error
@application.errorhandler(404)
def page_not_found(e):
    # here i created my own 404 page which will be redirect when 404 error occured in this web app
    return render_template("404.html"), 404

if __name__ == "__main__":
    application.run()