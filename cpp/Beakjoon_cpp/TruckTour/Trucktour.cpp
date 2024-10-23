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

int truckTour(vector<vector<int>> petrolpumps) {
    int n = petrolpumps.size();
    int result = -1;


    for (int i = 0; i < n; i++)
    {
        bool can_tour = true;
        int remain_petrol = 0;
        for (int j = i; j < n + i; j++)
        {
            remain_petrol += petrolpumps[j % n][0];
            if (remain_petrol - petrolpumps[j % n][1] < 0)
            {
                can_tour = false;
                break;
            }
            remain_petrol -= petrolpumps[j % n][1];
        }
        if (can_tour)
        {
            result = i;
            break;
        }
    }
    return result;
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<vector<int>> petrolpumps(n);

    for (int i = 0; i < n; i++) {
        petrolpumps[i].resize(2);

        string petrolpumps_row_temp_temp;
        getline(cin, petrolpumps_row_temp_temp);

        vector<string> petrolpumps_row_temp = split(rtrim(petrolpumps_row_temp_temp));

        for (int j = 0; j < 2; j++) {
            int petrolpumps_row_item = stoi(petrolpumps_row_temp[j]);

            petrolpumps[i][j] = petrolpumps_row_item;
        }
    }

    int result = truckTour(petrolpumps);

    cout << result << "\n";

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
