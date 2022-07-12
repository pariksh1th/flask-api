from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/gen")
def gen():
    return {"time": ["teff", "fucks", "working"]}

if __name__ == "__main__":
    app.run(debug=True)
    
    