from flask import Flask, render_template, request, jsonify,session,redirect
from flask_sqlalchemy import SQLAlchemy
from chat import get_response
from flask_mail import Mail
from flask import flash

import nltk_utils
import uuid
import json
#import train

app = Flask(__name__)


mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/feedback'
db = SQLAlchemy(app)


class Feedback(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
class Unanswer(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), unique=False, nullable=False)
    
class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(50), unique=False, nullable=False) 
    token= db.Column(db.String(50), unique=False, nullable=False) 
    password= db.Column(db.String(50), unique=False, nullable=False)   
app.secret_key ='super-secret-key'
admin=Admin.query.all()
for a in admin:
    email= a.email
    password= a.password
app.config.update(
    MAIL_SERVER ="smtp.gmail.com",
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = email,
    MAIL_PASSWORD = password
)
mail = Mail(app)

@app.get("/")
def index_get():
    return render_template("index.html")
@app.get("/addhtml")
def addhtml():
    if ('user' in session and session['user'] == params["email"]):
        return render_template("add.html")
    return render_template("admin.html")
@app.get("/deletehtml")
def deletehtml():
    if ('user' in session and session['user'] == params["email"]):
        return render_template("delete.html")
    return render_template("admin.html")
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    if (response=="I do not understand"):
        entry = Unanswer(question=text)
        db.session.add(entry)
        db.session.commit()

    message={"answer": response}
    return jsonify(message)

     
with open('intents.json','r+') as c:
    
    intent = json.load(c)    

@app.route("/j", methods=['GET','POST']) 
def j():
    if ('user' in session and session['user'] == params["email"]):
        return intent
    return render_template("admin.html")
@app.route("/add", methods=['GET','POST']) 
def add():
    with open('intents.json','r+') as c:
        temp = json.load(c)
    json_data={}
    json_data["patterns"]=request.form.getlist('keyword')
    json_data["responses"]=request.form.getlist('response')
    json_data["tag"]=request.form.get('tag')
    if ('user' in session and session['user'] == params["email"]):
        temp["intents"].append(json_data)
    else:
        return render_template("admin.html")
    with open('intents.json','w') as c:
        json.dump(temp,c,indent=4)
    return json_data

@app.route("/delete/<string:tag>", methods=['GET','POST']) 
def delete(tag):
    json_data=[]
    delete_option=tag
    if ('user' in session and session['user'] == params["email"]):
        for entry in intent["intents"]:
            
            if entry["tag"]== delete_option:
               
                pass
               
            else:
                json_data.append(entry)
        intent["intents"]=json_data
        with open('intents.json','w') as c:
            json.dump(intent,c,indent=4)
    else:
        return render_template("admin.html")
    return render_template("view.html")

@app.route("/admin", methods=['GET','POST'])     
def admin():
    admin = Admin.query.all()
    for a in admin:
           
            
        if ('user' in session and session['user'] == a.email):
        
            return render_template('view.html')
        if request.method=='POST':
            email = request.form.get('email')
            password = request.form.get('password')
            if  (email == a.email and password == a.password):
                session['user'] = email
            
                return render_template('view.html')
            else:
                flash("Invalid email or password", "warning")
                return render_template("admin.html") 
   
    return render_template('admin.html')
@app.route("/forgetpass", methods=['GET','POST'])     
def forgetpass():
    
    if request.method=='POST':
        email = request.form.get('email')
        token = str(uuid.uuid4())
       
        admin = Admin.query.all()
        for a in admin:
           
            if ( email== a.email):
                
                a.token=token
                db.session.commit()
                message = render_template("sent.html", token=token, admin=admin)
                mail.send_message("message from chatbot system", sender=email, recipients = email, body= "message")
                flash("check your email", "success")
                
            else:
                flash("Invalid email", "warning")
                return render_template("admin.html") 
   
    return render_template('forgetpass.html')

@app.route("/confirmpass/<token>", methods=['GET','POST'])     
def confirmpass(token):
    
    if request.method=='POST':
        password = request.form.get('password')
        confirmpass = request.form.get('confirm password')
        
        if password!=confirmpass:
            flash("confirm password not match","warning")
            return render_template("confirmpass.html")
       
        #admin = Admin.query.filter_by(token=token)
        admin = Admin.query.all()
        for a in admin:
           

            if (token==a.token):
            
                a.password=password
                db.session.commit()
               
                flash("your password successfully updated", "success")
                return render_template('admin.html')
            else:
                flash("your token is invalid", "warning")
                return render_template("forgetpass.html")
               
    return render_template("confirmpass.html")

@app.route("/jsontable", methods=['GET','POST'])
def jsontable():
    with open('intents.json','r') as c:
    
        intent = json.load(c)["intents"]    
    return render_template("json.html",intent=intent)
    
@app.route("/feedback_database", methods=['GET','POST'])
def feedback_database():
    feedback = Feedback.query.all()
    return render_template("database.html",feedback=feedback)
       
    
@app.route("/unanswer_database", methods=['GET','POST'])
def unanswer_database():
    unanswer = Unanswer.query.all()
    return render_template("unanswer.html",unanswer=unanswer)
    
   
@app.route("/logout")
def logout():
    session.pop('user')
    return render_template('admin.html')
@app.route("/deletedb1/<string:sno>" , methods=['GET', 'POST'])
def deletedb1(sno):
    
    feedback = Feedback.query.filter_by(sno=sno).first()
    db.session.delete(feedback)
    db.session.commit()
    return redirect("/feedback_database")
@app.route("/deletedb2/<string:sno>" , methods=['GET', 'POST'])
def deletedb2(sno):
    
    unanswer = Unanswer.query.filter_by(sno=sno).first()
    db.session.delete(unanswer)
    db.session.commit()
    return redirect("/unanswer_database")  
@app.route("/feedback", methods=['GET','POST'])
def feedback():
    if(request.method=="POST"):
        name = request.form.get("fullname")
        email1 = request.form.get("email")
        message = request.form.get("message")
        entry = Feedback(name = name, email = email1, message = message)
        db.session.add(entry)
        db.session.commit()
        
        mail.send_message("message from " + name, sender=email1, recipients = a.email, body= message)
        flash("feedback send successfully","success")
    return render_template("feedback.html") 

if __name__== "__main__":
    app.run(debug=True)