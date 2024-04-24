from flask import Flask
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

# Create a new client and connect to the server replace your own password with <password> 
client = MongoClient("mongodb+srv://f8th:<password>@f8thdb.dese96y.mongodb.net/test?retryWrites=true&w=majority&appName=f8thDB")

# Access the 'new_database' in your cluster
db = client['test']

# Access the 'new_collection' in 'new_database'
collection = db['todo_flask']

from application import routes
