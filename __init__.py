from flask import Flask, jsonify, render_template, redirect
import time
##########################################################

app = Flask(__name__)

ledStatus = 1

##########################################################


@app.route('/led-status')
def getStatus():
    status = ledStatus
    return jsonify (ledStatus = status)



@app.route('/button')
def getButton():
    return render_template('button.html', ledStatus=ledStatus)


@app.route('/led-swap')
def swapStatus():
    global ledStatus

    if ledStatus == 1:
        ledStatus = 0
    else:
        ledStatus = 1

    time.sleep(0.5)

    return render_template('button.html', ledStatus=ledStatus)


##########################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0')
