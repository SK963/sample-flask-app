from flask import Flask

app = Flask(__name__)



@app.route("/")
def home():
    return "Hello from Flask App : Shubham Kumar"


@app.route('/about')
def about():
    return "This is the About page of the Flask app built by shubham kumar."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
