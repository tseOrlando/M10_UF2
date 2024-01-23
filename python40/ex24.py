import json

def r_js():

    with open("ex23.json", "r") as f:
        print(json.load(f))

r_js()