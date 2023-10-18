class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 1:
            return 0
        odd = False
        even = False
        half = len(nums) //2
        if len(nums)%2: odd = True
        else: even = True
        def checker(num1 , num2):
            ans = 0
            ans += half + num1[0] 
            ans += half + num2[0]
            if odd:
                ans += 1
            return ans
        
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for i in range(0 , n , 2):
            count1[nums[i]] += 1
            if i != n -1:
                count2[nums[i + 1]] += 1
        
        
        heap1 = []
        heap2 = []
        for key , val in count1.items():
            heappush(heap1 , (-val , key))
        for key , val in count2.items():
            heappush(heap2 , (-val , key))
        ans = len(nums)
        ans1 = heappop(heap1)
        ans2 = heappop(heap2)
        if ans1[1] == ans2[1]:
            if heap2:
                val = checker(ans1 , heap2[0])
            else:
                val = half
            ans  = min(ans , val)
            if heap1:
                val = checker(heap1[0] , ans2)
            else:
                val = half
            ans = min(ans , val)
        else:
            val = checker(ans1 , ans2)
            ans = min(ans , val)
        
        return ans