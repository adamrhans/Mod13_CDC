import os
import sys
# import pymysql
# from cassandra.cluster import Cluster

# ------------------
# input arguments
# ------------------
# -create, create containers
# -delete, delete containers
# -init, init mysql and cassandra, others do not need it

# delete container
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')


# read input arguments
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]    

# if -create input arguement, create containers
if(argument == '-create'):
    # create('docker run -p 5600:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    create('docker run -p 1800:27017 --name final_mongo_container -d mongo', 'mongo')
    # create('docker run -p 2400:6379 --name final_redis_container -d redis', 'redis')
    # create('docker run -p 1000:9042 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()

# if -delete input argument, delete containers
if(argument == '-delete'):
    # delete('final_mysql_container')
    delete('final_mongo_container')
    # delete('final_redis_container')
    # delete('final_cassandra_container')
    sys.exit

