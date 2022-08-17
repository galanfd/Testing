import json

def toptweets():
    tweets = []

    with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    for i in tweets:
        print(i["retweetedTweet"])
    # newlist = sorted(tweets, key=lambda d: d['retweetedTweet'], reverse=True)
    # tweets.sort(key=lambda b: b['retweetedTweet'])
    # for i in range(0, 9):
    #     print(tweets[i]) 
    # return


toptweets()