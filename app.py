from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        users.append({
            "name": name,
            "email": email,
            "password": password
        })

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        for user in users:
            if user["email"] == email and user["password"] == password:
                return redirect(url_for("product"))

        return "Wrong email or password"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
