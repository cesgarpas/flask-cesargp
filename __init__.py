from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import time

############################# DB Set Up#############################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vlsisfddogfqxb:4bc16c307e949f3a9d4f3bdeef768c4f79b28348b1859d75875b59716a5377ca@ec2-176-34-184-174.eu-west-1.compute.amazonaws.com:5432/dbg9l15vcp6ai6'
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
