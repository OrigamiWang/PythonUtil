from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')


@app.route('/')
def index():  # put application's code here
    return render_template('templates/index.html')


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    temp_file_path = os.path.join(os.getcwd() + '\\file_save', file.filename)
    file.save(temp_file_path)
    return jsonify({"message": "File uploaded and saved successfully"})


if __name__ == '__main__':
    app.run()
