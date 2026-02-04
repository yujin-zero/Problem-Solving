#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (vector<int> c : commands) {
        int start_idx = c[0];
        int end_idx = c[1];
        int k = c[2];
                vector<int> lst;
        for (int i=start_idx-1; i<end_idx; i++) {
            lst.push_back(array[i]);
        }
        
        sort(lst.begin(), lst.end());
        answer.push_back(lst[k-1]);
    }
    
    return answer;
}