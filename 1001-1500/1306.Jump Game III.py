from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        # BFS
        visited = set()
        q = deque([start])
        n = len(arr)
        while q and len(visited) < n:
            cur = q.popleft()
            if cur not in visited:
                visited.add(cur)
                nexts = [cur - arr[cur], cur + arr[cur]]
                for nxt in nexts:
                    if 0 <= nxt < n and nxt not in visited:
                        if arr[nxt] == 0:
                            return True
                        q.append(nxt)
        return False
