import flask
from flask import Flask
import webview
import sys
import threading

# add system module path
sys.path.append('.')
# write logs to log.txt
sys.stdout = open("log.txt", "a")
sys.stderr = open("log.txt", "a")
# create flask app, set the url path, static folder path, template folder path
app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template('templates/index.html')


def start_server():
    app.run()


if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window("PyWebviewFlaskDemo", 'http://127.0.0.1:5000')  # 把app换成URL
    webview.start()
