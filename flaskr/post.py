import datetime
from mongoengine import *
from flaskr.user import User

class Post(Document):
    author_id = ReferenceField(User, reverse_delete_rule=CASCADE)
    timestamp = DateTimeField(default=datetime.datetime.now)
    title = StringField(max_length=120, required=True)
    body = StringField()

    meta = {
        'indexes': [
            '+timestamp'
        ]
    }
    
    def toDBCollection(self):
        return {
            'author_id': self.author_id,
            'timestamp': self.timestamp,
            'title': self.title,
            'body': self.body
        }
