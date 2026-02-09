#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int p_len = p.size();
    
    for (int i=0; i<t.size()-p_len+1; i++) {
        string tmp = "";
        for (int j=i; j<i+p_len; j++) {
            tmp += t[j];
        }
        if (tmp <= p) {
            answer++;
        }
    }

    return answer;
}