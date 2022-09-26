/*
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3

Constraints:
start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
*/
#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        set<string> bank_set(bank.begin(), bank.end());
        queue<string> q;
        q.push(start);
        int level = 0;
        const vector<char> chars { 'A', 'C', 'G', 'T' };
        while (!q.empty()) {
            int n = q.size();
            while (n--) {
                string s = q.front();
                if (s == end) {
                    return level;
                }
                q.pop();
                bank_set.erase(s);
                for (int i = 0; i < 8; i++) {
                    string temp = s;
                    for (auto c = chars.cbegin(); c != chars.cend(); c++) {
                        temp[i] = *c;
                        if (bank_set.find(temp) != bank_set.end()) {
                            q.push(temp);
                        }
                    }
                }
            }
            level++;
        }
        return -1;
    }
};

void case1() {
    vector<string> bank { "AACCGGTA" };
    string start { "AACCGGTT" }, end { "AACCGGTA" };
    Solution s;
    int result = s.minMutation(start, end, bank);
    cout << result << endl;
}

void case2() {
    vector<string> bank { "AACCGGTA","AACCGCTA","AAACGGTA" };
    string start { "AACCGGTT" }, end { "AAACGGTA" };
    Solution s;
    int result = s.minMutation(start, end, bank);
    cout << result << endl;
}

void case3() {
    vector<string> bank { "AAAACCCC","AAACCCCC","AACCCCCC" };
    string start { "AAAAACCC" }, end { "AACCCCCC" };
    Solution s;
    int result = s.minMutation(start, end, bank);
    cout << result << endl;
}

void case4() {
    vector<string> bank { "AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC" };
    string start { "AACCTTGG" }, end { "AATTCCGG" };
    Solution s;
    int result = s.minMutation(start, end, bank);
    cout << result << endl;
}

int main()
{
    case1();
    case2();
    case3();
    case4();
    return 0;
}
