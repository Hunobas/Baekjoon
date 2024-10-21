#include <iostream>
#include <string>
#include <vector>

using namespace std;

string ltrim(const string&);
string rtrim(const string&);
vector<string> split(const string&);

int flippingMatrix(vector<vector<int>> matrix) {
    int n = matrix.size() / 2;
    for (int i = 0; i < 2*n; i++)
    {
        int column_max = 0, max_index = 0;
        for (int j = 0; j < 2*n; j++)
        {
            if (matrix[j][i] > column_max)
            {
                column_max = matrix[j][i];
                max_index = j;
            }
        }
        if (max_index > n)
        {
            for (int j = 0; j < n; j++)
            {
                swap(matrix[j][i], matrix[2*n - 1- j][i]);
            }
        }
    }
    for (int j = 0; j < n; j++)
    {
        int left_sum = 0, right_sum = 0;
        for (int i = 0; i < n; i++)
        {
            left_sum += matrix[j][i];
            right_sum += matrix[j][2*n - 1 - i];
        }
        if (right_sum > left_sum)
        {
            for (int i = 0; i < n; i++)
            {
                swap(matrix[j][i], matrix[j][2*n - 1 - i]);
            }
        }
    }

    int result = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result += matrix[i][j];
        }
    }
    return result;
}

int main()
{
    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        vector<vector<int>> matrix(2 * n);

        for (int i = 0; i < 2 * n; i++) {
            matrix[i].resize(2 * n);

            string matrix_row_temp_temp;
            getline(cin, matrix_row_temp_temp);

            vector<string> matrix_row_temp = split(rtrim(matrix_row_temp_temp));

            for (int j = 0; j < 2 * n; j++) {
                int matrix_row_item = stoi(matrix_row_temp[j]);

                matrix[i][j] = matrix_row_item;
            }
        }

        int result = flippingMatrix(matrix);

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