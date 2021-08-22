from flask import Blueprint,request,json, render_template,redirect

from .extensions import mongo

main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        res = json.dumps(request.json)
        data = json.loads(res)
        print(res)
        if 'action' in data:
            author = data['pull_request']['base']['repo']['owner']['login']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            timestamp = data['pull_request']['base']['repo']['updated_at']
            request_id = data['pull_request']['base']['repo']['id']
            action = data['action']
            user_collection = mongo.db.git_hub
            user_collection.insert({'request_id':request_id,'author':author,'action':action,'from_branch':from_branch,'to_branch':to_branch,'timestamp':timestamp})
        else:
            author = data['commits'][0]['author']['name']
            from_branch = data['base_ref']
            to_branch = data['ref']
            timestamp = data['commits'][0]['timestamp']
            request_id = data['head_commit']['id']
            action = 'Push'
            user_collection = mongo.db.git_hub
            user_collection.insert({'request_id':request_id,'author':author,'action':action,'from_branch':from_branch,'to_branch':to_branch,'timestamp':timestamp})
            
    retrieve = mongo.db.git_hub.find()
    print(retrieve)
    return  render_template('index.html',retrieve=retrieve)