from collections import defaultdict
import heapq
from typing import List

class Twitter:
    """
    time complexity: O(logn) for heap operations
    overall time complexity: O(k)
    """

    def __init__(self):
        self.count = 0
        # userId -> list of [count, tweetId]
        self.tweet_map = defaultdict(list)
        # userId -> set of followerId
        self.follow_map = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        # since we need minHeap
        self.count -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = []
        # user follow themselves too
        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        print(minHeap)
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)