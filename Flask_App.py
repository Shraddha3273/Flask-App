from flask import Flask, jsonify, request


app = Flask(__name__)
task = [
    {
        'Id' : 1,
        'Name' : 'Seema',
        'Contact' : '9987644456',
        'Done' : False
    },

    {
        'Id' : 2,
        'Name' : 'Reema',
        'Contact' : '9876543222',
        'Done' : False
    }
]

# the following func. will allow post request on this route
@app.route("/add-data", methods=["POST"])
def add_task() : 
    if not request.json : 
        return jsonify({
            "status" : "ERROR",
            "message" : "PLEASE PROVIDE THE DATA!!"
        }, 400)
    newTask = {
        'id' : task[-1]['id']+1,
        'title' : request.json['title'],
        'description' : request.json.get('description', ""),
        'done' : False
        }

    task.append(newTask)
    return jsonify({
            "status" : "SUCCESS",
            "message" : "DATA ADDED SUCCESSFULLY!!"
    })

@app.route("/get-data")
def get_task() : 
    return jsonify({
        "data" : task
    })

if(__name__ == "__main__") : 
    app.run(debug=True)