from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for
import config
# import thinter as thinter
# from thinter import messagebox
import mysql.connector

app=Flask(
    __name__,
    # static_folder="static",
    # static_url_path="/"
)
app.secret_key="abc" #For session

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name=request.form["name"]
    userName=request.form["username"]
    passWord=request.form["password"]

    mydb=mysql.connector.connect(
        host=config.mysql["host"],
        user=config.mysql["user"],
        password=config.mysql["password"],
        database="mydatabase"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT username FROM member WHERE name= %s AND username= %s", (name, userName))#把name寫進來是避免出現這個錯誤：mysql.connector.errors.ProgrammingError: Could not process parameters: str(test), it must be of type list, tuple or dict
    mydbUserName=mycursor.fetchall()

    print(mydbUserName) #[('test'),('test')]=>list
    print(mydbUserName[0]) #('test',)=>tuple
    print(userName) #test=>str
    
    for x in mydbUserName:
        if userName in x:
            result="帳號已被註冊"
            return redirect(url_for('failed', message=result))
            break
        else:
            sql="INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
            val=(name,userName, passWord)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

            # thinter.messagebox.showinfo('Info','註冊成功')
            return redirect("/")
    #想直接使用SELECT進行username的重複確認=>攥寫中！(卡關在mysql只能process list, tuple, dict, 但username是str)
    # if userName in checkUserName:
    #     result="帳號已被註冊"
    #     return redirect(url_for('failed', message=result))
    # else:
    #     sql="INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
    #     val=(name, userName, passWord)
    #     mycursor.execute(sql, val)

    #     mydb.commit()
    #     print(mycursor.rowcount, "record inserted.")
    #     return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    userName=request.form["username"]
    passWord=request.form["password"]
    mydb=mysql.connector.connect(
        host=config.mysql["host"],
        user=config.mysql["user"],
        password=config.mysql["password"],
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name FROM member WHERE username= %s AND password= %s", (userName,passWord))
    mydbUserName=mycursor.fetchall()

    if mydbUserName==[]:
        condition="未登入"
        session["status"]=condition
        result="帳號、或密碼輸入錯誤"
        return redirect(url_for('failed',message=result))
    elif userName=="" or passWord=="":
        condition="未登入"
        session["status"]=condition
        result="請輸入帳號、密碼"
        return redirect(url_for('failed', message=result))#url_for('函式名稱', 參數)=>網址加變數字串
    else:
        condition="已登入"
        session["status"]=condition
        session["username"]=userName
        session["password"]=passWord
        print(mydbUserName)
        session["name"]=mydbUserName
        return redirect(url_for('success'))
        

@app.route("/member")
def success():
    if 'username' in session:
        print(type(session["username"]))
        print(session)
        result=','.join(session["name"][0])#將tuple轉換為str
        print(type(result))
        return render_template("success.html", name=result)#name is the what I put in html
    return redirect("/")

    # 也是使用request取得在後端宣告的參數
    # status=request.args.get("condition")
    # print(status)
    # if status == "未登入" or status == None:
    #     return redirect("/")
    # else:
    #     return render_template("success.html")

@app.route("/error")
def failed():
    message =request.args.get("message")
    return render_template("failed.html", message=message) #first message is what I put in html

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("username", None)
    session["status"]="未登入"
    print(session["status"])
    return redirect("/")

app.run(port=3000)