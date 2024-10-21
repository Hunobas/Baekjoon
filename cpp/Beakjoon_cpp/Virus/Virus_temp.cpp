#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Graph
{
public:
	Graph(int computers)
	{
		for (int i = 1; i <= computers; i++)
		{
			path[i] = vector<int>();
		}
	}

	const unordered_map<int, vector<int>>& GetPath() const { return path; }

	void AddEdge(const int& u, const int& v)
	{
		// In case of inter-direction Graph
		path[u].push_back(v);
		path[v].push_back(u);
	}

private:
	unordered_map<int, vector<int>> path;
};

class Virus
{
public:
	int Solution(Graph* G)
	{
		unordered_set<int> empty_visited;
		vector<int> result;

		dfs(G, 1, empty_visited, result);

		// execpt computer 1
		return result.size() - 1;
	}

private:
	void dfs(Graph* G, const int& start, unordered_set<int>& visited, vector<int>& result)
	{
		// if there is already in visited, end recursion
		if (visited.count(start))
		{
			return;
		}

		visited.insert(start);
		result.push_back(start);

		for (int next : G->GetPath().at(start))
		{
			dfs(G, next, visited, result);
		}
	}
};

int main()
{
	int computers, connections;

	cin >> computers >> connections;
	Graph G = Graph(computers);

	for (int i = 0; i < connections; i++)
	{
		int u, v;
		cin >> u >> v;
		G.AddEdge(u, v);
	}

	Virus sol;
	cout << sol.Solution(&G) << endl;

	return 0;
}