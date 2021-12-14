import flask
import random
import string
import os

from utils import Config

allowedFiletypes = ["png", "jpg", "jpeg", "gif", "webm", "mp4"]
blueprint = flask.Blueprint("upload", __name__)

def isAllowed(filename):
    extension = filename.split(".")[-1]
    if extension in allowedFiletypes:
        return True
    return False

def alreadyExists(filename):
    if os.path.isfile(f"uploads/{filename}"):
        return True
    return False

def randomString(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))

@blueprint.route("/upload", methods=["POST"])
def upload():
    uploadedFile = flask.request.files["file"]
    if "upload-key" not in flask.request.form: return flask.jsonify({"error": "No upload key provided."})
    uploadKey = flask.request.form["upload-key"]

    if not uploadKey or uploadKey != Config.UPLOAD_KEY: return flask.jsonify({"error": "Invalid upload key"})
    if not uploadedFile: return flask.jsonify({"error": "No file uploaded"})
    if not isAllowed(uploadedFile.filename): return flask.jsonify({"error": "Filetype not allowed"})

    extension = uploadedFile.filename.split(".")[-1]
    hashedName = randomString(8) + "." + extension

    while alreadyExists(hashedName): hashedName = randomString(8) + "." + extension

    uploadedFile.save("uploads/" + hashedName)
    return flask.jsonify({"success": "File uploaded", "filename": hashedName, "url": f"http://{Config.MAIN_DOMAIN}/" + hashedName})
