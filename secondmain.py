import json

def not_following_back(following, followers):
    following_ids = set(user['string_list_data'][0]['value'] for user in following)
    followers_ids = set(user['string_list_data'][0]['value'] for user in followers)
    return following_ids - followers_ids

with open("following.json", "r") as following_file:
    following = json.load(following_file)['relationships_following']
with open("followers.json", "r") as followers_file:
    followers = json.load(followers_file)

result = not_following_back(following, followers)
print("Users not following back:", result)
