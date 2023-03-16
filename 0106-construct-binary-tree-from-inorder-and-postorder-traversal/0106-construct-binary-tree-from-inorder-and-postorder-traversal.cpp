class Solution {
public:
    int findPos(vector<int> &in, int ele, int n){
        for(int i=0; i<n; i++){
            if(in[i] == ele)
                return i;
        }
        return -1;
    }
    
    TreeNode* f(vector<int>& inorder, vector<int>& postorder, int &index, int left, int right, int n){
        if(left > right) 
            return NULL;

        int val = postorder[index];
        
        TreeNode* root = new TreeNode(val);
        int idx = findPos(inorder, val, n);
        index--;
        
        root -> right = f(inorder, postorder, index, idx + 1, right, n);
        root -> left  = f(inorder, postorder, index, left,   idx - 1, n);

        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int idx = n-1;
        TreeNode* res = f(inorder, postorder, idx, 0, idx, n);
        return res;
    }
};