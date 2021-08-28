from ast import Index
from flask import Blueprint
from flask import json
from flask import render_template
from flask import url_for
from flask import request
import pymongo
import math
from .extensions import mongo

main = Blueprint('main',__name__)

@main.route('/',defaults={'limitx':'2','offsetx':'0'} ,methods=['GET','POST'])
@main.route('/<int:limitx>/<int:offsetx>',methods=['GET','POST'])
def index(limitx,offsetx):
    if request.method == 'POST':

        data = json.loads(request.json)
        print(data)
    # Updating Mongodb with data 
        if 'action' in data:
            author = data['pull_request']['base']['repo']['owner']['login']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            timestamp = data['pull_request']['base']['repo']['updated_at']
            request_id = data['pull_request']['base']['repo']['id']
            action = data['action']
            user_collection = mongo.db.git_hub
            user_collection.insert({
                'request_id':request_id,
                'author':author,
                'action':action,
                'from_branch':from_branch,
                'to_branch':to_branch,
                'timestamp':timestamp})
        else:
            check_merge = data['commits'][2]['message'].split(' ')

            if check_merge[0] == 'Merge':
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Merge'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})
            else:
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Push'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})

    # Pagination 
            
    git_user = mongo.db.git_hub

    limit = int(limitx)
    offset = int(offsetx)

    pagination = math.ceil(int(git_user.find().count())/limit)

    starting_id = git_user.find().sort('_id',pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']

    retrieve = git_user.find({'_id':{'$gte':last_id}}).sort('_id',pymongo.ASCENDING).limit(limit)

    next_url = url_for('main.index',limitx=2,offsetx=offset+limit)
    prev_url = url_for('main.index',limitx=2,offsetx=offset-limit)
    page_role = None
    return  render_template('index.html',retrieve=retrieve,next_url=next_url,prev_url=prev_url,pagination=pagination,limit=limit,page_role=page_role)



@main.route('/admin/',defaults={'limitx':'2','offsetx':'0'},methods=['GET','POST'])
@main.route('/admin/<int:limitx>/<int:offsetx>',methods=['GET','POST'])
def admin(limitx,offsetx):
    if request.method == 'POST':

        data = json.loads(request.json)
    # Updating Mongodb with data 
        if 'action' in data:
            author = data['pull_request']['base']['repo']['owner']['login']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            timestamp = data['pull_request']['base']['repo']['updated_at']
            request_id = data['pull_request']['base']['repo']['id']
            action = data['action']
            user_collection = mongo.db.git_hub
            user_collection.insert({
                'request_id':request_id,
                'author':author,
                'action':action,
                'from_branch':from_branch,
                'to_branch':to_branch,
                'timestamp':timestamp})
        else:
            check_merge = data['commits'][2]['message'].split(' ')

            if check_merge[0] == 'Merge':
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Merge'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})
            else:
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Push'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})

    # Pagination 
            
    git_user = mongo.db.git_hub

    limit = int(limitx)
    offset = int(offsetx)

    pagination = math.ceil(int(git_user.find().count())/limit)

    starting_id = git_user.find().sort('_id',pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']

    retrieve = git_user.find({'_id':{'$gte':last_id}}).sort('_id',pymongo.ASCENDING).limit(limit)

    next_url = url_for('main.admin',limitx=2,offsetx=offset+limit)
    prev_url = url_for('main.admin',limitx=2,offsetx=offset-limit)

    #Page Role
    page_role='Admin'
    return render_template('index.html',retrieve=retrieve,next_url=next_url,prev_url=prev_url,pagination=pagination,limit=limit,page_role=page_role)



@main.route('/super_admin/',defaults={'limitx':'2','offsetx':'0'},methods=['GET','POST'])
@main.route('/super_admin/<int:limitx>/<int:offsetx>',methods=['GET','POST'])
def superadmin(limitx,offsetx):
    if request.method == 'POST':

        data = json.loads(request.json)
    # Updating Mongodb with data 
        if 'action' in data:
            author = data['pull_request']['base']['repo']['owner']['login']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            timestamp = data['pull_request']['base']['repo']['updated_at']
            request_id = data['pull_request']['base']['repo']['id']
            action = data['action']
            user_collection = mongo.db.git_hub
            user_collection.insert({
                'request_id':request_id,
                'author':author,
                'action':action,
                'from_branch':from_branch,
                'to_branch':to_branch,
                'timestamp':timestamp})
        else:
            check_merge = data['commits'][2]['message'].split(' ')

            if check_merge[0] == 'Merge':
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Merge'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})
            else:
                author = data['commits'][0]['author']['name']
                from_branch = data['base_ref']
                to_branch = data['ref'].split('/')[-1]
                timestamp = data['commits'][0]['timestamp']
                request_id = data['head_commit']['id']
                action = 'Push'
                user_collection = mongo.db.git_hub
                user_collection.insert({
                    'request_id':request_id,
                    'author':author,
                    'action':action,
                    'from_branch':from_branch,
                    'to_branch':to_branch,
                    'timestamp':timestamp})

    # Pagination 
            
    git_user = mongo.db.git_hub

    limit = int(limitx)
    offset = int(offsetx)

    pagination = math.ceil(int(git_user.find().count())/limit)

    starting_id = git_user.find().sort('_id',pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']

    retrieve = git_user.find({'_id':{'$gte':last_id}}).sort('_id',pymongo.ASCENDING).limit(limit)

    next_url = url_for('main.superadmin',limitx=2,offsetx=offset+limit)
    prev_url = url_for('main.superadmin',limitx=2,offsetx=offset-limit)

    #Page Role
    page_role='Super Admin'
    return render_template('index.html',retrieve=retrieve,next_url=next_url,prev_url=prev_url,pagination=pagination,limit=limit,page_role=page_role)
