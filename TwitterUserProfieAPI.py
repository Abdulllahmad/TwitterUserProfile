# Here I Used tweepy to get user information from twitter by using Twitter API key 
# Don't forget YOU SHOULD PAY FOR API KEY TO USE THIS CODE!!
# https://developer.twitter.com/en/portal/dashboard
# Put your KEYS in line 10-13 Inside "" :)



import tweepy

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to get profile information for a user
def get_profile_info(username):
    try:
        user = api.get_user(username)
        profile_info = {
            'Username': user.screen_name,
            'Number of Tweets': user.statuses_count,
            'Number of Followers': user.followers_count,
            'Date Joined Twitter': user.created_at
        }
        return profile_info
    except tweepy.TweepError as e:
        print(f"Error: {e}")

# List of usernames to retrieve profile info for
usernames = [
    "user1",
    "user2",
    "user3",
    # Add more usernames here
]

# Retrieve profile info for each username
profile_infos = []
for username in usernames:
    profile_info = get_profile_info(username)
    if profile_info:
        profile_infos.append(profile_info)

# Print profile info for each user
for profile_info in profile_infos:
    print(profile_info)
