import sys
from collections import defaultdict ,deque
n = int(input())
graph = defaultdict(list)
indegree = defaultdict(int)
queue = deque()
words = []
for _ in range(n):
    word = input()
    words.append(word)

for idx in range(n - 1):
    if words[idx][0] != words[idx+ 1][0]:
        graph[words[idx][0]].append(words[idx + 1][0])
        indegree[words[idx + 1][0]] += 1
    else:
        for i , l in enumerate(words[idx]):
            if i == len(words[idx +1]):
                print("Impossible")
                sys.exit()
            if words[idx][i] != words[idx + 1][i]:
                graph[words[idx][i]].append(words[idx + 1][i])
                indegree[words[idx + 1][i]] += 1
                break
for letter in range(26):
    let = chr(letter + 97)
    if let not in indegree:
        queue.append(let)
ans = ""
while queue:
    letter = queue.popleft()
    ans += letter
    for val in graph[letter]:
        indegree[val] -= 1
        if indegree[val] == 0:
            queue.append(val)

if len(ans) == 26:
    print(ans)
else:
    print("Impossible")