class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        def backtrack(arr , path):
            if len(arr)== n:
                self.ans += 1
            for idx in range(1,n + 1):
                if idx not in path:
                    if idx % (len(arr) + 1) ==0 or (len(arr) + 1) % idx ==0:
                        arr.append(idx)
                        path.add(idx)
                        backtrack(arr , path)
                        path.remove(idx)
                        arr.pop()
        backtrack([] ,set())
        return self.ans