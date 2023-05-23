#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
        from collections import defaultdict , deque
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        for idx in range(N - 1):
            if alien_dict[idx][0] != alien_dict[idx+ 1][0]:
                graph[alien_dict[idx][0]].append(alien_dict[idx + 1][0])
                indegree[alien_dict[idx + 1][0]] += 1
            else:
                for i , l in enumerate(alien_dict[idx]):
                    if i == len(alien_dict[idx +1]):
                        return []
                    if alien_dict[idx][i] != alien_dict[idx + 1][i]:
                        graph[alien_dict[idx][i]].append(alien_dict[idx + 1][i])
                        indegree[alien_dict[idx + 1][i]] += 1
                        break
        
        for letter in range(k):
            let = chr(letter + 97)
            if let not in indegree:
                queue.append(let)
        
        ans = [] 
        
        while queue:
            letter = queue.popleft()
            ans.append(letter)
            for val in graph[letter]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
        
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends