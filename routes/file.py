import flask

from utils import Config

blueprint = flask.Blueprint("file", __name__)

@blueprint.route("/<filename>", methods=["GET"])
def get(filename):
    rawurl = "raw/" + filename
    if Config.TWITTER_CARDS:
        return flask.render_template("preview.html", filename=filename, rawurl=rawurl, rawurlfull=f"http://{Config.MAIN_DOMAIN}/" + rawurl)
    else:
        return flask.send_from_directory("uploads", filename)

@blueprint.route("/raw/<filename>", methods=["GET"])
def raw(filename):
    return flask.send_from_directory("uploads", filename)