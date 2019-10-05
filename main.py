from flask import Flask, render_template, request, redirect
from data import USERS
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/users/")
def users():
    return render_template("user_list.html", users=USERS)


@app.route("/user_form/", methods=["GET", "POST"])
def user_form():
    if request.method == "GET":
        return render_template("user_form.html")

    if not request.form["name"] or not request.form["age"]:
        return render_template("user_form.html", attention="fields name and age are required")

    user = dict(
        name=request.form["name"],
        surname = request.form["surname"],
        age = request.form["age"]
    )
    USERS.append(user)

    return redirect("/users/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)















# @app.route("/user/")
# @app.route("/user/<name>")
# def get_user(name=None):
#     if name:
#         return f'''
#             <h1>User {name}</h1>'''
#     return '''
#         <ul>
#             <li>
#                 <a href="/user/Harry">Harry</a>
#             </li>
#             <li>
#                 <a href="/user/Hermiona">Hermiona</a>
#             </li>
#             <li>
#                 <a href="/user/Rohn">Rohn</a>
#             </li>
#         </ul>
#         '''


# @app.route("/user/")
# @app.route("/user/<name>")
# def user(name=None):
#     if name:
#         return render_template("user_form.html", user_name=name)
#     return render_template("user_list.html")