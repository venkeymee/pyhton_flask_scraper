# Python code to illustrate the Modules
from dbmodel.Dbconnection import DbConnection
from parserservice.browser import Browser
from parserservice.input_maper import RequestMap
import json


def bs4ParseInit(url):
    print("parese url:"+url);
    dbconnection=DbConnection()
    parsed_html=Browser().get_browser(url);
    textData=parsed_html.body.text
    # dbconnection=DbConnection();

    for index,line in enumerate(textData.split('\n')):
        # print("lineNumber:"+str(index)+":data:"+line)
        try:
            record={}
            record['id']='INDEX_'+str(index)
            for index,params in enumerate(line.split(',')):
                # print(str(index)+":"+params)
                params=params.replace('"', '').replace('\\','')
                record[RequestMap.numbers_to_strings(index)]=params

            # save record into DB
            # record=json.dumps(record, default=lambda o: o.__dict__)
            print(record)
            dbconnection.save(dbconnection.container,record)
        except Exception as e:
            print(e)


class Pareser:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self,url):
        self.url=url;
        # A normal print function

    def pareseDataFromURL(self):
        print('parese method init')
        bs4ParseInit(self.url)

        # for model in self.models:
        #     print('\t%s ' % model)