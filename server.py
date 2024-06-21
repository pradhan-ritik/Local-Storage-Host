import shutil
from flask import Flask, render_template, request, url_for
from werkzeug.datastructures import FileStorage
import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload_file', methods=('POST',))
def upload_one():
    print(request.files)
    if 'file' in request.files:
        file_ = request.files['file']
        path = f"files/{file_.filename}"
        data = file_.save(path)
        api.encode(path)
        api.remove(path)

        return 'File uploaded successfully'

    return "wassup"
    

if __name__ == "__main__":
    app.run(debug=True)