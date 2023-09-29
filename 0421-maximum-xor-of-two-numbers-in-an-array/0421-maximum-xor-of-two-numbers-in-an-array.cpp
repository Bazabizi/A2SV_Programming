#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class TrieNode {
public:
    vector<TrieNode*> children;

    TrieNode() {
        children = vector<TrieNode*>(2, nullptr);
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(int size, int num) {
        TrieNode* node = root;
        for (int i = size; i >= 0; i--) {
            int bit = (num >> i) & 1;

            if (!node->children[bit]) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
        }
    }

    int search(int size, int num) {
        TrieNode* node = root;
        int ans = 0;
        for (int i = size; i >= 0; i--) {
            int bit = (num >> i) & 1;

            if (node->children[1 - bit]) {
                ans += (1 << i);
                node = node->children[1 - bit];
            }
            else {
                node = node->children[bit];
            }
        }
        return ans;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int ans = 0;
        Trie trie;
        int size = 31;
        
        for (int num : nums) {
            trie.insert(size, num);
        }

        for (int num : nums) {
            ans = max(ans, trie.search(size, num));
        }
        return ans;
    }
};