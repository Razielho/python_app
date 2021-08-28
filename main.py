from os import error
import mongoengine
import sys
#from mongoengine.connection import connect, disconnect
from mongoengine import *
import yaml
import json
import logging
import datetime

#logger initialization
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(handlers=[logging.FileHandler('mongoengine.log', 'w', 'utf-8')],level=logging.INFO,format=FORMAT)
log=logging.getLogger()

def connect2mongo():
    try:
        mydb=connect(host="mongodb://admin:admin@localhost:27027/test?authSource=admin")
        log.info("connection established to default datatbase")
    except:
        log.error("connection error",error)
        exit(8)
    return mydb

class Comment(EmbeddedDocument):
    content = StringField()

class Page(DynamicDocument):
    title = StringField(max_length=200, required=True, unique=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=15))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'collection': 'cmsPage'}

class User(Document):
    name = StringField()

class Page2(Document):
    content = StringField()
    author = ReferenceField(User)
    boss = ReferenceField('self')

#class ProfilePage(Document):
#    content = StringField()

class Employee(Document):
    name = StringField()
    boss = ReferenceField('self')
#    profile_page = ReferenceField('ProfilePage')

class ProfilePage(Document):
    employee = ReferenceField(Employee, reverse_delete_rule=mongoengine.CASCADE)
    content = StringField()


### main program ###
def main():

    log.info("program started")
    mydb=connect2mongo()

    """
    comment1 = Comment(content='Good work!')
    comment2 = Comment(content='Nice article!')

    page = Page(title='Using MongoEngine with embedded', \
        tags = ['one', 'two'],
        comments=[comment1, comment2])
    page.tags = ['mongodb', 'mongoengine']
    page.save()

    print(Page.objects(tags='mongoengine').count())

    john = User(name="John Smith")
    john.save()

    post = Page2(content="Test Page")
    post.author = john
    post.save()
    """

    Tamar=Employee(name="Tamar")
    Tamar.save()
    
    myProfile=ProfilePage(content="Tamar profile page content")
    myProfile.employee=Tamar
    myProfile.save()
    
    Tamar.delete()
    
    
    # read yaml configuration file
    # params=read_configuration_file()
    # print(params)
    
    disconnect(mydb)
    log.info("closing connection to default database")
    log.info("program ended")
    
if __name__ == "__main__":
    main()