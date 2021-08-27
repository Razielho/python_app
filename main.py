from os import error
import mongoengine
import sys
from mongoengine.connection import connect, disconnect
import yaml
import json
import logging

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

### main program ###
def main():

    log.info("program started")
    mydb=connect2mongo()


    # read yaml configuration file
    # params=read_configuration_file()
    # print(params)
    
    disconnect(mydb)
    log.info("closing connection to default database")
    log.info("program ended")
    
if __name__ == "__main__":
    main()