import flask

blueprint = flask.Blueprint("index", __name__)

@blueprint.route("/")
def index():
    return flask.render_template("index.html")