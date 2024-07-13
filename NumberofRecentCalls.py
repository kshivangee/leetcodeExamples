from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.recent_requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.recent_requests.append(t)
        while(t-self.recent_requests[0]>3000):
            self.recent_requests.popleft()
        return len(self.recent_requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)