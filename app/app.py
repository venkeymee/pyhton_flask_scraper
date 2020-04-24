from flask import Flask,request
from parserservice.parseurl import Pareser
from parserservice.service_read import ServiceReadData
from flask import jsonify
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/parseUrl',methods=['GET','POST'])
def parseDataFronURL():
    inputReq=request.get_json();
    inputReq=inputReq['URL']
    # 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
    parse=Pareser(inputReq)
    parse.pareseDataFromURL();
    return "Success"

@app.route('/getDoc',methods=['GET','POST'])
def getItemByDocId():
    inputReq = request.get_json()
    inputReq=inputReq['document']
    service=ServiceReadData();
    data=service.getDocById(inputReq['document'])
    return jsonify(data);
#
@app.route('/getAlldoc',methods=['GET','POST'])
def getAllDocs():
    service = ServiceReadData()
    data=service.getAllDocs()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8443')
