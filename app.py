
from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)


# Create client and db
client = MongoClient('localhost', 27017)
db = client.task_database 
todos = db.todos 


# Get and Post 
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":  
        task = request.form['task']
        degree = request.form['degree']
        todos.insert_one({'task': task, 'degree': degree})
        return redirect(url_for('index')) 
    all_todos = todos.find()   
    
    return render_template('index.html', todos = all_todos)

#Delete 
@app.post("/<id>/delete/")
def delete(id): 
    todos.delete_one({"_id":ObjectId(id)}) 
    return redirect(url_for('index')) 

if __name__ == "__main__":
    app.run(debug=True)# the server will automatically reload for code changes and show a debugger in case an exception happened.