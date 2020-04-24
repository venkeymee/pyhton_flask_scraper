from dbmodel.Dbconnection import DbConnection



class ServiceReadData:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.connection=DbConnection();
        # A normal print function

    def getDocById(self,docId):
        return self.connection.readByDoc(docId);

    def getAllDocs(self):
        return self.connection.readAllDoc();
