from global_imports import *

# reads all the database and shows it by console

def read():
    send.execute("SELECT * FROM public.users")

    for user in send.fetchall():
        print(f"id : {user[0]}\nname : {user[1]}\npassword : {user[2]}\nage : {user[3]}\ngender : {user[4]}\nrange : {user[5]}\n")