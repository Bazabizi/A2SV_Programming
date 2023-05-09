class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heappush(heap , (nums1[0] + nums2[0] , 0 , 0))
        length1 = len(nums1)
        length2 = len(nums2)
        ans = []
        visited = set()
        while heap and len(ans) < k:
            min_sum , idx1 , idx2 = heappop(heap)
            ans.append([nums1[idx1] , nums2[idx2]])
            if idx1 + 1 < length1 and (idx1 + 1 , idx2) not in visited:
                heappush(heap ,(nums1[idx1 + 1] +  nums2[idx2] , idx1 + 1 , idx2))
                visited.add((idx1+ 1 , idx2))
            if idx2 + 1 < length2 and (idx1 , idx2 + 1) not in visited:
                heappush(heap ,(nums2[idx2 + 1] +  nums1[idx1] , idx1 , idx2 + 1))
                visited.add((idx1 , idx2 + 1))
        return ans