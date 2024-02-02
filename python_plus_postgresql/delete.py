from global_imports import *

def delete(id):
    send.execute(f"DELETE FROM public.users WHERE user_id={id}")