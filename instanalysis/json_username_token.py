import json


def get_token_and_username(json_file):

    json_data = json.loads(json_file)

    username = json_data['user']['username']
    access_token = json_data['access_token']
    return username, access_token

