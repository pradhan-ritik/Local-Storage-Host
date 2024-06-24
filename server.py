import os
from flask import Flask, render_template, request, send_file, url_for
import api

app = Flask(__name__)

@app.route('/')
def home():
    files, folders = [], []
    for i in os.listdir("files"):
        if i.endswith(".tar.xz"):
            files.append(i)
        else:
            folders.append(i)
    return render_template("index.html", path="", files=files, folders=folders)

@app.route('/upload_files/', methods=('POST',))
def upload_files_root():
    uploaded = ""

    data = request.files.getlist("files")
    for file_ in data:
        path = os.path.join("files/", file_.filename)
        data = file_.save(path)
        api.encode(path)
        api.remove(path)
        uploaded += f"{file_.filename}  "

    return render_template("upload_files/index.html", uploaded=uploaded)

@app.route('/make_folder/', methods=('POST',))
def make_folder_root():
    folder_name = f"files/{request.form.get('folder_name')}"
    if os.path.exists(folder_name):
        return render_template("make_folder/index.html", folder_name="ERROR: FILE ALREADY EXISTS")
    os.mkdir(folder_name)
    return render_template("make_folder/index.html", folder_name=folder_name)

@app.route('/download/<path>')
def download(path: str):
    real_path = f"files/{path}.tar.xz"
    download_path = f"tmp"
    path_to = f"{download_path}/files/{path}"
    api.decode(real_path, download_path)
    send_path = api.encode_for_user(path_to, f"{download_path}/files")

    if send_path != path_to:
        api.remove(path_to)

    return send_file(send_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)