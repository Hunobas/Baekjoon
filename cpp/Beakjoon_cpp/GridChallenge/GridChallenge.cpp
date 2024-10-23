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

string gridChallenge(vector<string> grid) {
    int n = grid.size();
    for (string& alpha : grid)
    {
        sort(alpha.begin(), alpha.end());
    }
    for (int i = 0; i < n; i++)
    {
        int ord;
        for (int j = 0; j < n - 1; j++)
        {
            ord = static_cast<int>(grid[j][i]);
            if (ord > static_cast<int>(grid[j + 1][i])) return "NO";
        }
    }
    return "YES";
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

        vector<string> grid(n);

        for (int i = 0; i < n; i++) {
            string grid_item;
            getline(cin, grid_item);

            grid[i] = grid_item;
        }

        string result = gridChallenge(grid);

        cout << result << "\n";
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
