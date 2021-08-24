import json
import os

def import_to_env():
    json_open = open('local.settings.json', 'r')
    json_load = json.load(json_open)
    values_dict = json_load['Values']

    for key in values_dict.keys():
        os.environ[key] = values_dict[key]
        print(f'env set: {key} = {os.environ[key]}' )
