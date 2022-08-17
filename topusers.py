import json
from collections import Counter

def topusers():
    tweets = []

    with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    cnt = Counter()
    for i in tweets:
        cnt[i['user']['username']] += 1
    for i in range(0, 9):
        print(cnt[i])


topusers()