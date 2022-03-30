from flask import Flask
app = Flask(__name__)

from pathlib import Path
from dotenv import load_dotenv

env_path = Path("example.env").resolve()
load_dotenv(dotenv_path=env_path)

try:
    import tracepointdebug
    tracepointdebug.start()
except ImportError as e:
    pass

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)