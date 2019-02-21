from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    msg_body = request.form['Body']

    #msg_body = msg_body.split()
    resp = MessagingResponse()
    resp.message(reply(msg_body))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)