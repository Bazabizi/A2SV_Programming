#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<pair<pair<int, int>, int>> graph;
    
    for (int i = 0; i < m; i++) {
        int start, end, width;
        cin >> start >> end >> width;
        graph.push_back(make_pair(make_pair(start, end), width));
    }
    
    vector<int> distances(n + 1, INT_MAX);
    distances[1] = 0;
    
    
    
    for (int i = 0; i < n - 1; i++) {
        for (auto edge : graph) {
            int start = edge.first.first;
            int end = edge.first.second;
            int width = edge.second;
            
            if (distances[start] != INT_MAX && distances[start] + width < distances[end]) {
                distances[end] = distances[start] + width;
            }
        }
    }
    for (int i = 0; i < n + 1; i++) {
        if (distances[i] == INT_MAX) {
            distances[i] = 30000;
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << distances[i] << " ";
    }
    
    return 0;
}
