"""
Aiden Duval's Flask API.
"""

from flask import Flask, abort, send_from_directory, render_template
import config
import os

app = Flask(__name__)

options = config.configuration()

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<filename>")
def serve(filename):
    file_path = os.path.join('pages/', filename)
    if ".." in filename or "~" in filename:
        abort(403)
    elif os.path.exists(file_path):
        return send_from_directory('pages/', filename), 200
    else:
        abort(404)
    
@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=options.DEBUG, host='0.0.0.0',port=options.PORT)
