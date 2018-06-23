# flask-cesargp
This contains an application configured to run on Heroku which its only variable on DB is the status of a LED (0 or 1). The arduino retrieves periodically information with a GET petition and sets it on or off.
On the heroku app on url /button there is a button for changing the led status.
