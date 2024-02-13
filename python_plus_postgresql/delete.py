from global_imports import *

# deletes a user by its user_id

def delete(id):
    send.execute(f"DELETE FROM public.users WHERE user_id={id}")