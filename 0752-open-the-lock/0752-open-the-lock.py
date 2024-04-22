class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        depth = -1
        visited, q = set(deadends), deque(['0000'])

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                if node == target: return depth
                if node in visited: continue
                visited.add(node)
                q.extend(self.successors(node))
        return -1

    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res