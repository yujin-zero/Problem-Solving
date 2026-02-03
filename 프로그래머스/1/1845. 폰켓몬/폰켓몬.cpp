#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int type_cnt = 0;
    int N = nums.size();
    vector<int> lst;
    
    for (int n : nums) {
        if (find(lst.begin(), lst.end(), n) == lst.end()) {
            lst.push_back(n);
        }
    }
    
    type_cnt = lst.size();
    
    if (type_cnt >= N/2) {
        return N/2;
    } else {
        return type_cnt;
    }
}