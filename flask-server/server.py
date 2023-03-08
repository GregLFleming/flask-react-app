from flask import Flask, request, Response
from cs50 import SQL
import json

app = Flask(__name__)

db = SQL("sqlite:///switchboard.db")

@app.route("/addDonation", methods=['POST'])
def addDonation():

    #Get the content type from the incoming POST request
    content_type = request.headers.get('Content-Type')

    #Check if the content type is of type JSON
    if (content_type == 'application/json'):

        #If the content is of type JSON, store that content inside a variable
        donation = request.json
        date = donation["contribution"]["createdAt"]
    #Return error message
    else:
        return 'Content-Type not supported!'
    
    db.execute("INSERT INTO donations (date, jsonData) VALUES(:date, :storedContent)", date = date, storedContent = json.dumps(donation))

    return Response("Sucessfully created a donation in the database", status=201, mimetype='application/json')

@app.route("/findDonations", methods=['GET'])
def getDonation():
    days_donations = int(request.args.get("parameter1"))

    if days_donations == 1:
        answer = db.execute("SELECT * FROM donations WHERE date > date('now','-1 days') ORDER BY ID DESC")
        return answer
    elif days_donations == 7:
        answer = db.execute("SELECT * FROM donations WHERE date > date('now','-7 days') ORDER BY ID DESC")
        return answer
    elif days_donations == 99:
        answer = db.execute("SELECT * FROM donations")
        return answer
    else:
        return Response("Bad Request", status=400, mimetype='application/json')





if __name__ == "__main__":
    app.run(debug=True)

    # list_qty = request.args.get("parameter1")