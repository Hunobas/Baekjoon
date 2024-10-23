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
long long pow_int(const int& base, const int& exponent, const int& MOD)
{
    long long result = 1;
    for (int i = 0; i < exponent; i++)
    {
        result = (result * base) % MOD;
    }
    return result;
}

int legoBlocks(int n, int m) {
    const int MOD = 1000000007;

    vector<long long> single_row(m + 1, 0);
    single_row[0] = 1;
    for (int i = 1; i <= m; i++) {
        for (int block = 1; block <= 4 && block <= i; block++) {
            single_row[i] = (single_row[i] + single_row[i - block]) % MOD;
        }
    }

    vector<long long> total(m + 1, 0);
    for (int i = 1; i <= m; i++) {
        total[i] = pow_int(single_row[i], n, MOD);
    }

    vector<long long> valid(m + 1, 0);
    valid[1] = total[1];
    for (int i = 2; i <= m; i++) {
        valid[i] = total[i];
        for (int j = 1; j < i; j++) {
            long long invalid = (valid[j] * total[i - j]) % MOD;
            valid[i] = ((valid[i] - invalid) + MOD) % MOD;
        }
    }

    return valid[m];
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);

        int m = stoi(first_multiple_input[1]);

        int result = legoBlocks(n, m);

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
