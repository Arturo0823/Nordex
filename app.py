from flask import Flask, request, jsonify

from flask_cors import CORS
import os

import smtplib
from email.message import EmailMessage



app = Flask(__name__)


CORS(app)



@app.route("/contact", methods=["POST"])


def conatct():
  data = request.json()
  name = data.get("name")

  email = data.get("email")


  message = data.get("message")



  if not name or not email or not message:
    return jsonify({"eror ": "Missing fields"}), 400 
  


  msg = EmailMessage() 

  msg["Subject"] = "New Nordex Contact" 



  msg['From'] = os.getenv("Email_USER") 
  msg['To'] = os.getenv("EMAIL_USER") 

  msg.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")


  with smtplib.SMTP_SSL("smtp.gmail.com",  465) as smtp:
    smtp.login(os.getenv("EMAIL_USER"),  os.getenv("EMAIL_PASSWORD"))


    smtp.send_message(msg)


    return jsonify("success": True)
  
  