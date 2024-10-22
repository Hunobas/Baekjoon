#include <iostream>
#include <vector>
#include <tuple>
#include <deque>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;
using it_iv_map = unordered_map<int, tuple<int, vector<int>>>;

class Graph
{
public:
	Graph(const int& nums)
	{
		length = nums;
	}

	const it_iv_map& GetPath() const { return popul_path; }
	const unsigned int GetLength() const { return length; }
	const unsigned int GetTotalPopul() const { return total_popul; }

	void SetPopul(const int& i, const int& popul)
	{
		popul_path[i] = make_tuple(popul, vector<int>());
		total_popul += popul;
	}

	void AddEdge(const int& u, const int& v)
	{
		if (u > length || v > length) return;
		get<1>(popul_path[u]).push_back(v);
	}

	vector<int> DFS(int start, unordered_set<int>& visited, vector<int>& result)
	{
		if (visited.count(start)) return result;

		visited.insert(start);
		result.push_back(start);

		for (int next: get<1>(popul_path[start]))
		{
			DFS(next, visited, result);
		}
		return result;
	}

	vector<int> BFS(int start)
	{
		vector<int> result;
		unordered_set<int> visited;
		deque<int> nexts;

		result.push_back(start);
		visited.insert(start);
		nexts.push_back(start);

		while (!nexts.empty())
		{
			int now = nexts.front();
			nexts.pop_front();
			for (int next : get<1>(popul_path[now]))
			{
				if (!visited.count(next))
				{
					result.push_back(next);
					visited.insert(next);
					nexts.push_back(next);
				}
			}
		}
		return result;
	}

	int GetWardPopul(vector<int> group)
	{
		int result = 0;
		for (int i : group)
		{
			result += get<0>(popul_path[i]);
		}
		return result;
	}

private:
	unsigned int length = 0;
	unsigned int total_popul = 0;
	it_iv_map popul_path;
};

void Solutoin(Graph* G, const vector<int>& populs);
int GetDifferenceOfTwoConstituencies(Graph* G, const vector<int>& populs);

int main() {
	int N;
	cin >> N;

	Graph G(N);
	vector<int> populs;

	for (int i = 1; i <= N; i++)
	{
		string popul;
		cin >> popul;
		G.SetPopul(i, stoi(popul));
		populs.push_back(stoi(popul));
	}

	for (int i = 1; i <= N; i++)
	{
		string connections;
		cin >> connections;

		for (int j = 0; j < stoi(connections); j++)
		{
			string path;
			cin >> path;
			G.AddEdge(i, stoi(path));
		}
	}

	if (N < 2)
	{
		cout << -1 << endl;
		return 0;
	}

	Solutoin(&G, populs);

	return 0;
}

void Solutoin(Graph* G, const vector<int>& populs)
{
	vector<vector<int>> graph_group;
	unordered_set<int> visited;

	for (int i = 1; i <= G->GetLength(); i++)
	{
		if (!visited.count(i))
		{
			vector<int> group;
			G->DFS(i, visited, group);
			graph_group.push_back(group);
		}
	}

	int num_group = graph_group.size();
	if (num_group == 0 || num_group > 2)
	{
		cout << -1 << endl;
	}
	else if (num_group == 2)
	{
		cout << abs(G->GetWardPopul(graph_group[0]) - G->GetWardPopul(graph_group[1])) << endl;
	}
	else if (num_group == 1)
	{
		cout << GetDifferenceOfTwoConstituencies(G, populs) << endl;
	}
}

int GetDifferenceOfTwoConstituencies(Graph* G, const vector<int>& populs)
{
	vector<int> result;

	unordered_set<int> visited;
	deque<int> nexts;
	int total_popul = G->GetTotalPopul();

	for (int start = 1; start <= G->GetLength(); start++)
	{
		int popul_wardA = 0;
		visited.clear();
		nexts.clear();

		visited.insert(start);
		nexts.push_back(start);

		while (!nexts.empty())
		{
			int now = nexts.front();
			nexts.pop_front();

			popul_wardA += get<0>(G->GetPath().at(now));
			if (popul_wardA >= total_popul / 2) break;

			for (int next : get<1>(G->GetPath().at(now)))
			{
				if (!visited.count(next))
				{
					visited.insert(next);
					nexts.push_back(next);
				}
			}
		}
		int difference = abs(2*popul_wardA - total_popul);
		result.push_back(difference);
		if (difference == 0) return 0;
	}
	return *min_element(result.begin(), result.end());
}