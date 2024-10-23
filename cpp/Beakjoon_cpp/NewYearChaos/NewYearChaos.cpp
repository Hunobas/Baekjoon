#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>
#include <vector>
#include <unordered_map>

using namespace std;

string ltrim(const string&);
string rtrim(const string&);
vector<string> split(const string&);

/*
 * Complete the 'lonelyinteger' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */


void minimumBribes(vector<int> q) {
    vector<int> sorted_q = q;
    sort(sorted_q.begin(), sorted_q.end());

    unordered_map<int, int> bribe_count;
    int result = 0;

    for (int i = q.size() - 1; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (q[j] > q[j + 1])
            {
                bribe_count[q[j]] += 1;
                result++;
                swap(q[j], q[j + 1]);
            }
            if (bribe_count[q[j + 1]] > 2)
            {
                cout << "Too chaotic" << endl;
                return;
            }
        }
    }
    cout << result << endl;
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        string q_temp_temp;
        getline(cin, q_temp_temp);

        vector<string> q_temp = split(rtrim(q_temp_temp));

        vector<int> q(n);

        for (int i = 0; i < n; i++) {
            int q_item = stoi(q_temp[i]);

            q[i] = q_item;
        }

        minimumBribes(q);
    }

    return 0;
}

string ltrim(const string& str) {
    string s(str);
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) {
        return !std::isspace(ch);
        }));
    return s;
}

string rtrim(const string& str) {
    string s(str);
    s.erase(
        std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
            return !std::isspace(ch);
            }).base(),
                s.end()
                );
    return s;
}

vector<string> split(const string& str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
