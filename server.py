import os
from flask import Flask, render_template, request, send_file, url_for
from werkzeug.datastructures import FileStorage
import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", files=map(api.tar_xz_path_to_normal, os.listdir("files/")))

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

@app.route('/download/<filename>')
def download(filename: str):
    real_path = f"files/{filename}.tar.xz"
    download_path = f"tmp/"
    api.decode(real_path, download_path)
    return send_file(f"{download_path}/files/{filename}", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)