#importing libraries, flask and aws
from flask import Flask, render_template, request,redirect, url_for
import boto3

app = Flask(__name__)

#config our database (DynamoDB)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('python_data')


#Routes
# '/' - home page
@app.route('/')
def index():
    return render_template('index.html')

# '/add' - add a new item to the database
@app.route('/add', methods=['POST'])
def add():
    data = {
        'Phone' : request.form['phone'],
        'Name' : request.form['name'],
    }

    #add the data to the database
    table.put_item(Item=data)

    return render_template('index.html')

# '/list' - list all items in the database
@app.route('/list')
def list():
    #get all items from the database
    response = table.scan()
    items = response['Items']

    return render_template('list.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)