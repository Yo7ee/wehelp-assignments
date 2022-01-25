from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

app=Flask(
    __name__,
    # static_folder="static",
    # static_url_path="/"
)
app.secret_key="abc" #For session

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    userName=request.form["username"]
    session["username"]=userName
    passWord=request.form["password"]
    session["password"]=passWord

    if userName=="test" and passWord=="test":
        condition="已登入"
        session["status"]=condition
        return redirect("/member")
    elif userName=="" or passWord=="":
        condition="未登入"
        session["status"]=condition
        result="請輸入帳號、密碼"
        return redirect(url_for('failed', message=result))#url_for('函式名稱', 參數)=>網址加變數字串
    else:
        condition="未登入"
        session["status"]=condition
        result="帳號、或密碼輸入錯誤"
        return redirect(url_for('failed',message=result))

@app.route("/member")
def success():
    print(session)
    if 'username' in session:
        return render_template("success.html")
    return redirect("/")


@app.route("/error")
def failed():
    message =request.args.get("message")
    return render_template("failed.html", message=message)

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("username", None)
    session["status"]="未登入"
    print(session["status"])
    return redirect("/")

app.run(port=3000)