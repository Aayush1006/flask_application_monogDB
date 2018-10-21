from flask import Flask, render_template,request
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('ds133113.mlab.com:33113')
db = client["newsreader"]
db.authenticate("aayush_91","Aashu@31")


##client = MongoClient('mongodb://aayush_91:Aashu@31@ds133113.mlab.com:33113')
##db = client.ContactDB

app = Flask(__name__, template_folder="templates")

@app.route('/',methods = ['GET', 'POST'])

def home():
    if request.method == 'POST':
        textValue = request.form['searchText']
        return search_user_details(textValue)
    elif request.method == 'GET':
        content = get_all_details()
        return render_template('home.html',content=content)

def get_all_details():
   return fetch_info() 

def search_user_details(textValue):
    content = fetch_info()
    search_list = []
    print(textValue)
    for result in content:
        if textValue in ''.join(result['headline']).lower():
            search_list.append(result)
    print("result list: ",search_list)
    return render_template('search.html',content=search_list)
def fetch_info():
    try:
        contacts = db.newsreader.find()
        return contacts
    except (Exception) as e:
        return dumps({'error' : str(e)})

if __name__ == '__main__':
    app.run(debug=True)


