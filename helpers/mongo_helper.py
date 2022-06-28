import pymongo


class MongoHelper:


    def __init__(self, url = "mongodb://localhost:27017/") -> None:
        self.myclient = pymongo.MongoClient(url)
        self.mydb = self.myclient["pracujPL"]
        self.mycol = self.mydb["jobtitles"]
        self.mycol2 = self.mydb["offers"]
        
