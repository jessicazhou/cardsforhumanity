
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("about to get ad...")
    ad = get_ad()
    api.update_status(ad)
    #time.sleep(INTERVAL)