from flask import Flask, request, jsonify  


app = Flask(__name__)



@app.route("/contact", methods=["POST"])

def conact():
  data = request.json
  name = data.get("name")
  email = data.get("email")
  message = data.get("message")



  if not name or not email or not message:
    return jsonify({"error": "Missing fields"}),  400  
  
  return jsonify({"Sucess": "Missing fields"}), 400 

  return jsonify({"sucess": True})