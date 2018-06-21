from flask import Flask, jsonify, render_template, redirect
##########################################################

app = Flask(__name__)

ledStatus = 1

##########################################################


@app.route('/led-status')
def getStatus():
    return jsonify (ledStatus = ledStatus)



@app.route('/button')
def getButton():
    return render_template('button.html', ledStatus=ledStatus)


@app.route('/led-swap')
def swapStatus():
    global ledStatus

    if ledStatus:
        ledStatus = 0
    else:
        ledStatus = 1

    return redirect("/button")


##########################################################

if __name__ == "__main__":
    app.run(debug=True)
