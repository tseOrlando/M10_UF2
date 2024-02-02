from global_imports import *

# inserts a new user, you must specify all the attributes
def create(id, user_name, password, user_age, gender, range):
    
    send.execute(f"INSERT INTO public.users(user_id, user_name, password, user_age, gender, \"range\") VALUES({id}, '{user_name}', '{password}', '{user_age}', '{gender}', '{range}')")
    peer.commit()