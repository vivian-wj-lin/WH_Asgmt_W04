
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

app.secret_key = "secret"

IS_LOGIN = "isLogin..."


@app.route("/")
def index():
    return render_template("W4.html")


@app.route("/member")
def index_member():
    if session.get(IS_LOGIN, None):
        return render_template("member.html")
    return redirect("/")
   

@app.route("/signout")
def signout():
    session[IS_LOGIN] = False  # 設定登出為 False
    return redirect("/")


@app.route("/signInFailure")
def index_signInFailure():
    return render_template("signInFailure.html")


@app.route("/signin", methods=["POST"])
def signin():
    accountName = request.form["accountName"]
    password = request.form["password"]
    if (accountName == "" or password == ""):
        return render_template("signInFailure.html", reason="請輸入帳號、密碼")
    elif (accountName == "test" and password == "test"):
        session[IS_LOGIN] = True  # 設定登入成功為 True
        return redirect("/member")
    elif (accountName != "test" or password != "test"):
        return render_template("signInFailure.html", reason="帳號、或密碼輸入錯誤")


app.run(port=3000)

# python W4.py
