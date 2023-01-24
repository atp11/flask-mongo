from mongoengine import *

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    
    def toDBCollection(self):
        return {
            'username': self.username,
            'password': self.password
        }