from global_imports import *

# updates user gender by its 'user_id'

def update(id, gender):
    
    send.execute(f"UPDATE public.users SET gender='{gender}' WHERE user_id='{id}'")
    peer.commit()