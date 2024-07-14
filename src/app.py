from flask import Flask
from src.resources.api import identify
from src.databases import db
from src.config import Config

app = Flask(__name__)

# load the configs
app.config.from_object(Config)

# init db
db.init_app(app)

app.register_blueprint(identify)

@app.route("/", methods=["GET", "POST"])
def check():
    return "Up and Running..."


if __name__ == "__main__":
    app.run()