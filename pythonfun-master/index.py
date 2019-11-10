from flask import Flask, render_template, request

app = Flask("My App")

@app.route("/")
def hello():
    return hello_someone("")

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"

app.run(debug=True)
