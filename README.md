# Change Data Capture (CDC)
---
### Data Engineering Tools Used:
- Use Python to create docker containers running on specified ports
- Use decorators to pass commands via python for the following:
  - -init
  - create
  - delete
- Using a python time loop class timer to simulate periodic writes and reads to the database

### Overview:

#### Part 1

- Add a file called my_sql_container.py and write the code to run a MySQL container. Use port 5600 and name your container final_mysql_container. 
- In a Terminal window, run the my_sql_container.py file using the create parameter to create a Docker container. 
- Create another file called my_mongo_container.py and write the code to run a MongoDB container. Use port 1800 and name your container final_mongo_container. 
- In a Terminal window, run the my_mongo_container.py file using the create parameter to create a Docker container. 
- In the same folder, create another file called my_redis_container.py and write the code to run a Redis container. Use port 2400 and name your container final_redis_container. 
- In a Terminal window, run the my_redis_container.py file using the create parameter to create a Docker container. 
- Create another file called my_cassandra_container.py and write the code to run a Cassandra container. Use port 1000 and name your container final_cassandra_container. 
- In a Terminal window, run the my_cassandra_container.py file using the create parameter to create a Docker container. 
- Delete all the containers you have created so far. You can choose to do this manually in Docker. 
- In the second part of the assignment, you will initialize and perform CDC on a MongoDB database.

#### Part 2

- Create a file called container.py. Ensure that it creates all the containers defined above using the same parameters as in Part 1 of this final assignment. 
- Run the container.py file in Docker to show that all the containers have been created successfully.
- Create a file called mysqldb.py and run this file a few times in your Terminal window. 
- Create a file called mongocdc.py and run this file a few times in your Terminal window. Use the create parameter. 
- In the same folder, create the scheduler.py file. Also note that the scheduler.py file is the controller. It controls the calls to the different databases to read and write, and it uses the time loop Python class timer to simulate periodic writes and reads to the database. 
- Run the container.py Python program from the command prompt passing -init as a parameter. 
- Run the scheduler.py Python program from the Terminal window. 
