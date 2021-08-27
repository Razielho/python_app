import mongoengine
import sys
import yaml
import json
import logging

#logger initialization
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(handlers=[logging.FileHandler('mongoengine.log', 'w', 'utf-8')],level=logging.INFO,format=FORMAT)
log=logging.getLogger()

### main program ###
def main():

    log.info("program started")

    # read yaml configuration file
    # params=read_configuration_file()
    # print(params)
    
    # list projects 4 ingests
    #projectList=get_projects_list(params['sourceDir'])
    #print(projectList)
    #download_biosamples(projectList,params['sourceDir'])
    
    log.info("program ended")
    
if __name__ == "__main__":
    main()