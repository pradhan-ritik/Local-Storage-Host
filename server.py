from flask import Flask, render_template, request, send_file, url_for
from werkzeug.datastructures import FileStorage
import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload_files', methods=('POST',))
def upload_folder():
    uploaded = ""

    data = request.files.getlist("files")
    for file_ in data:
        path = f"files/{file_.filename}"
        data = file_.save(path)
        api.encode(path)
        api.remove(path)
        uploaded += f"{file_.filename}  "

    return render_template("upload_files/index.html", uploaded=uploaded)

if __name__ == "__main__":
    app.run(debug=True)