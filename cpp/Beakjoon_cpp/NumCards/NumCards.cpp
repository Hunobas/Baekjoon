#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string ltrim(const string&);
string rtrim(const string&);
vector<string> split(const string&);

bool BinarySearch(vector<int> arr, int target)
{
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else if (arr[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            return true;
        }
    }
    return false;
}

void NumCards(vector<int> cards, vector<int> inputs)
{
    for (int i : inputs)
    {
        cout << BinarySearch(cards, i) << ' ';
    }
}

int main()
{
    string n_temp, m_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    getline(cin, m_temp);
    int m = stoi(ltrim(rtrim(m_temp)));

    string b_temp_temp;
    getline(cin, b_temp_temp);

    vector<string> b_temp = split(rtrim(b_temp_temp));

    vector<int> b(m);

    for (int i = 0; i < m; i++) {
        int b_item = stoi(b_temp[i]);

        b[i] = b_item;
    }
    sort(a.begin(), a.end());
    NumCards(a, b);

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