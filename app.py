from flask import Flask, render_template
#from flask_wtf import FlaskForm
import datetime
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)

cred = credentials.Certificate("sampleflaskdemo-firebase-adminsdk-aurqr-f91bf3c4e3.json")
firebase_admin.initialize_app(cred, {"storageBucket": "sampleflaskdemo.appspot.com"})
bucket = storage.bucket()

@app.route("/")
def index():
    image_path="images/pexels-sumeet-ahire-15542925.jpg"
    try:
        blob = bucket.blob(image_path)
        image_url = blob.generate_signed_url(expiration=datetime.timedelta(minutes=15), method="GET")
        print("Generated URL:", image_url)
        return render_template("index.html", image_url=image_url)
    except Exception as e:
        return str(e)

if __name__=="__main__":
    app.run()