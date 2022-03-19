import os
import sys
import pymysql
from cassandra.cluster import Cluster

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

def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='MyNewPass',
        host='127.0.0.1',
        port=5600)

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    # use db
    query = ("USE pluto")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(50),
        stamp VARCHAR(40)
    )
    ''')
    cursor.execute(query)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()

# initialize cassandra db
def init_cassandra():
    keyspace = None
    cluster = Cluster(['localhost'], port=1000)
    session = cluster.connect(keyspace)

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS stamps
        WITH REPLICATION = {'class':'SimpleStrategy','replication_factor' :1};
        """)

    session.set_keyspace('stamps')
    session.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id text  PRIMARY KEY,
            stamp text
        );
        """)

    session.execute(f"insert into posts (id, stamp) values ('maxTimeStamp', '1975-01-01 00:00:00') IF NOT EXISTS")

# read input arguments
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]    

# if -create input arguement, create containers
if(argument == '-create'):
    create('docker run -p 5600:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    create('docker run -p 1800:27017 --name final_mongo_container -d mongo', 'mongo')
    create('docker run -p 2400:6379 --name final_redis_container -d redis', 'redis')
    create('docker run -p 1000:9042 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit

# if -init, init database
if(argument == '-init'):
    init_mysql()
    init_cassandra()
    sys.exit