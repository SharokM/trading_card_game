from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def renderTemplateRoute():
    return render_template("villain.html")

# Run the flask server
if __name__ == "__main__":
    app.run()