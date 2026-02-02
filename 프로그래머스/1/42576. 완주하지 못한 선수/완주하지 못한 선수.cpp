#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    int N = completion.size();
    for (int i=0; i<N; i++) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
    
    return participant[N];
}