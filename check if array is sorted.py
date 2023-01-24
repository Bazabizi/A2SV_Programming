#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for idx in range(n-1):
            if arr[idx]>arr[idx+1]:
                return 0
        return 1
