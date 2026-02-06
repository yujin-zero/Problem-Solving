#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    vector<int> v(n+2, 1);
    v[0] = 0;
    v[n+1] = 0;
    
    for (int l : lost) {
        v[l] -= 1;
    }
    for (int r : reserve) {
        v[r] += 1;
    }
    
    for (int i=1; i<n+1; i++) {
        if (v[i] > 0) {
            answer += 1;
        } else {
            if (v[i-1] > 1) {
                v[i-1] -= 1;
                v[i] += 1;
                answer += 1;
            } else if (v[i+1] > 1) {
                v[i+1] -= 1;
                v[i] += 1;
                answer += 1;
            }
        }
    }
    
    return answer;
}