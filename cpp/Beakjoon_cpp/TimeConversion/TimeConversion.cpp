#include <string>
#include <iostream>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    string result = s.substr(0, s.size() - 2);
    int hour = stoi(result.substr(0, 2));
    if (toupper(s[s.size() - 2]) == 'P' && hour != 12)
    {
        string military_hour = to_string(hour);
        result.replace(0, 2, to_string(hour + 12));
    }
    else if (toupper(s[s.size() - 2]) == 'A' && hour == 12)
    {
        result.replace(0, 2, "00");
    }

    return result;
}

int main()
{
    string s;
    getline(cin, s);

    string result = timeConversion(s);

    cout << result << "\n";

    return 0;
}
