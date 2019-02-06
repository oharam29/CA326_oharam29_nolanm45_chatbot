from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from testing import *

app = Flask(_name_)


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    msg_body = request.form['Body']

    msg_body = msg_body.split()
    resp = MessagingResponse()
    resp.message(print_trains(msg_body[0], msg_body[1]))

    return str(resp)


if _name_ == "_main_":
    app.run(debug=True)