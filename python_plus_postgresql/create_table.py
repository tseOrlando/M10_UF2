from global_imports import *

def create_table():

    if (input("do you want to create 'users' table? y/n\n") == 'y'):
        send.execute("""CREATE TABLE users(user_id SERIAL PRIMARY KEY, user_name VARCHAR(255) NOT NULL, 
                        password VARCHAR(255) NOT NULL, user_age BIGINT NOT NULL, gender VARCHAR(1) NOT NULL, 
                        range BIGINT NOT NULL);""")
        peer.commit()