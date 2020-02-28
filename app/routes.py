from flask import json, Response

from app import app, db
from app.database import ListTable, LinkTable, AssociationTable
import app.application as application


@app.route('/')
def index():
    return "Number of lists is {}, number of links is {}".format(ListTable.query.count(), LinkTable.query.count())


@app.route('/lists', methods=['GET'])
def lists():
    return application.get_lists()



@app.route('/create/<name>/<description>', methods=['GET'])
def create(name, description):
    return application.create_list(name, description)



@app.route('/add/<list_name>/<link_name>/<link_url>', methods=['GET'])
def add_link(list_name, link_name, link_url):
    return application.add_link(list_name, link_name, link_url)


@app.route('/get/<name>', methods=['GET', 'OPTIONS'])
def get_list(name: str) -> Response:
    response = Response(response=json.dumps(application.get_list(name)))
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5000'
    # response.headers['Content-Type'] = 'application/json';
    print(response.data)
    return response
