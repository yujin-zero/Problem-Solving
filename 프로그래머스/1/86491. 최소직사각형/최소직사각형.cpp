#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max_long = 0;
    int max_short = 0;
    
    for (vector<int> size : sizes) {
        int w = size[0];
        int h = size[1];
        
        int l = max(w, h);
        int s = min(w, h);
        
        max_long = max(max_long, l);
        max_short = max(max_short, s);
    }
    
    answer = max_long * max_short;
    
    return answer;
}