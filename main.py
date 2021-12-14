import os
import flask
import importlib

app = flask.Flask(__name__, template_folder="templates/")

for routeFile in os.listdir("routes"):
    if routeFile.endswith(".py"):
        lib = importlib.import_module(f"routes.{routeFile[:-3]}")
        app.register_blueprint(getattr(lib, "blueprint"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)