#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> supo1 = {1, 2, 3, 4, 5};
    vector<int> supo2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> supo3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    int idx1 = 0;
    int idx2 = 0;
    int idx3 = 0;
    
    int collect1 = 0;
    int collect2 = 0;
    int collect3 = 0;
    
    for (int a : answers) {
        int value1 = supo1[idx1];
        int value2 = supo2[idx2];
        int value3 = supo3[idx3];
        
        if (value1 == a) {
            collect1 += 1;
        } 
        if (value2 == a) {
            collect2 += 1;
        }
        if (value3 == a) {
            collect3 += 1;
        }
        
        idx1 += 1;
        idx2 += 1;
        idx3 += 1;
        
        if (idx1 == supo1.size()) {
            idx1 = 0;
        }
        if (idx2 == supo2.size()) {
            idx2 = 0;
        }
        if (idx3 == supo3.size()) {
            idx3 = 0;
        }
    } 
    
    int max_collect = max({collect1, collect2, collect3});
    if (collect1 == max_collect) {
        answer.push_back(1);
    }
    if (collect2 == max_collect) {
        answer.push_back(2);
    }
    if (collect3 == max_collect) {
        answer.push_back(3);
    }
    
    return answer;
}