import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.myTweets = defaultdict(list)
        self.myFollows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.myTweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.myTweets[userId].copy()

        if self.myFollows[userId]:
            for user in self.myFollows[userId]:
                if user == userId:
                    continue
                else:
                    tweets += self.myTweets[user].copy()
        heapq.heapify_max(tweets)

        output = []

        count = 10
        while tweets and count > 0:
            output.append(heapq.heappop_max(tweets)[1])
            count -= 1

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.myFollows[followerId]:
            return
        self.myFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.myFollows[followerId]:
            return
        self.myFollows[followerId].remove(followeeId)
