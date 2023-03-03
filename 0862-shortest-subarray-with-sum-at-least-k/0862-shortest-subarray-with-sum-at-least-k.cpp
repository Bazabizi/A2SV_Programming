class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        deque<int>store;
        vector<long long>prefixSum(nums.size() + 1,0);
        for(int i = 1; i <nums.size()+1; i++ ){
            prefixSum[i] = prefixSum[i-1] + nums[i-1];
        }
    
        int ans = INT_MAX;
        for (int i= 0 ; i < prefixSum.size(); i++){
            
            while(!store.empty() && prefixSum[i] - prefixSum[store.front()] >=k ){
                ans = min(ans,i - store.front());
                    store.pop_front();
                
            }
            while(!store.empty() && prefixSum[store.back()] >= prefixSum[i] ){
                store.pop_back();
            }
            
            store.push_back(i);
        }
        
        if (ans==INT_MAX){
            return -1;
        }
        return ans;
    }
};