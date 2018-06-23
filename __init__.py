from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import time

############################# DB Set Up#############################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://imkvanaqhxfquj:d8a0710bf1e7f1f95d0a9f38017d05035827ba36a98031ea3b5f156e64de13fa@ec2-54-247-100-44.eu-west-1.compute.amazonaws.com:5432/d27b1kimhdmc6p'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
db = SQLAlchemy(app)

############################ Model ##############################

class LED(db.Model):
    status = db.Column('status', db.Integer, primary_key=True)

############################ Routes ##############################


@app.route('/led-status')
def getStatus():
    status = LED.query.first().status
    return jsonify (ledStatus = status)



@app.route('/button')
def getButton():
    status = LED.query.first().status
    return render_template('button.html', ledStatus=status)


@app.route('/led-swap')
def swapStatus():
    led = LED.query.first()

    if led.status == 1:
        led.status = 0
    else:
        led.status = 1

    db.session.commit()

    time.sleep(0.5)
    return redirect("/button")


########################### Init ###############################

if __name__ == "__main__":
    db.create_all()
    objects = LED.query.all()
    if objects == None:
        ledStatus = LED(status=1)
        db.session.add(ledStatus)
        db.session.commit()
    app.run()#host='0.0.0.0')#, debug=True)
