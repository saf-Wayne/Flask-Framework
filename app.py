from flask import Flask
from path import path

app = Flask(__name__)
app.register_blueprint(path, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)      #Turn debug off for production environment