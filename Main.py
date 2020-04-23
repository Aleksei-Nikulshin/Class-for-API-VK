from urllib.parse import urlencode
import requests
import json

# APP_ID = 7401274
# user_id = 105375047
# OAUTH_URL = 'https://oauth.vk.com/authorize'
# OAUTH_PARAMS = {
#      'client_id': APP_ID,
#      'user_id': user_id,
#      'display': 'page',
#      'scope': 'status, friends, offline',
#      'response_type': 'token',

#      'v': '5.103'
#  }


# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))


TOKEN = "7a550ce4f044288571781153da1c64b34c0238c5242988c5c417af5f9305a81ad82053f28af9fcf85c63a"

# response = requests.get('https://api.vk.com/method/users.get?user_id=105375047&',
#                         params={'access_token': TOKEN, 'v': 5.103})


class User():

    def __init__(self, token, user_id):
        self.token = token
        self.id = user_id

    def __str__(self):
        return str(f'https://vk.com/id{self.id}')

    def get_id(user):
        resp = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': TOKEN,
                'user_id': user.id,
                'v': 5.103
            }
        )
        return resp.json()['response']['items']

    def __and__(self, user):
        user_id = set(self.get_id())
        user_2_id = set(user.get_id())
        mutual_list = list(user_id & user_2_id)
        print(mutual_list)
        return mutual_list


user_1 = User(TOKEN, 105375047)
user_2 = User(TOKEN, 351416577)

user_1 & user_2

print(user_1)