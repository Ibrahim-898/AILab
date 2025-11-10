import heapq

# Heuristic: Manhattan distance
def heuristic(state, goal):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(state[i]), 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

# Get neighbors
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # empty tile
    x, y = divmod(idx, 3)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

# A* algorithm
def a_star(start, goal):
    heap = []
    heapq.heappush(heap, (heuristic(start, goal), 0, start, []))  # (f, g, state, path)
    visited = set()

    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(heap, (new_f, new_g, neighbor, path + [state]))

    return None  # No solution

# Example usage
start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal_state  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution_path = a_star(start_state, goal_state)

if solution_path:
    print("Steps to solve the puzzle:")
    for step in solution_path:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print("----")
else:
    print("No solution found.")





# #include <bits/stdc++.h>
# using namespace std;

# // Manhattan distance heuristic
# int heuristic(const vector<int>& state, const vector<int>& goal) {
#     int dist = 0;
#     for (int i = 0; i < 9; ++i) {
#         if (state[i] != 0) {
#             int x1 = i / 3, y1 = i % 3;
#             int pos = find(goal.begin(), goal.end(), state[i]) - goal.begin();
#             int x2 = pos / 3, y2 = pos % 3;
#             dist += abs(x1 - x2) + abs(y1 - y2);
#         }
#     }
#     return dist;
# }

# // Get neighbors by sliding the empty tile (0)
# vector<vector<int>> get_neighbors(const vector<int>& state) {
#     vector<vector<int>> neighbors;
#     int idx = find(state.begin(), state.end(), 0) - state.begin();
#     int x = idx / 3, y = idx % 3;
#     vector<pair<int,int>> moves = {{-1,0},{1,0},{0,-1},{0,1}}; // Up, Down, Left, Right

#     for (auto [dx, dy] : moves) {
#         int nx = x + dx, ny = y + dy;
#         if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
#             int nidx = nx*3 + ny;
#             vector<int> new_state = state;
#             swap(new_state[idx], new_state[nidx]);
#             neighbors.push_back(new_state);
#         }
#     }
#     return neighbors;
# }

# // Node for priority queue
# struct Node {
#     vector<int> state;
#     int g, f;
#     vector<vector<int>> path;

#     bool operator>(const Node& other) const {
#         return f > other.f;
#     }
# };

# // A* algorithm
# vector<vector<int>> a_star(const vector<int>& start, const vector<int>& goal) {
#     priority_queue<Node, vector<Node>, greater<Node>> pq;
#     set<vector<int>> visited;

#     pq.push({start, 0, heuristic(start, goal), {start}});

#     while (!pq.empty()) {
#         Node current = pq.top(); pq.pop();

#         if (current.state == goal) return current.path;
#         if (visited.count(current.state)) continue;
#         visited.insert(current.state);

#         for (auto neighbor : get_neighbors(current.state)) {
#             if (!visited.count(neighbor)) {
#                 int new_g = current.g + 1;
#                 int new_f = new_g + heuristic(neighbor, goal);
#                 vector<vector<int>> new_path = current.path;
#                 new_path.push_back(neighbor);
#                 pq.push({neighbor, new_g, new_f, new_path});
#             }
#         }
#     }
#     return {}; // No solution
# }

# // Print a state
# void print_state(const vector<int>& state) {
#     for (int i = 0; i < 9; ++i) {
#         cout << state[i] << " ";
#         if (i % 3 == 2) cout << endl;
#     }
#     cout << "----\n";
# }

# int main() {
#     vector<int> start_state = {1,2,3,4,0,5,6,7,8};
#     vector<int> goal_state  = {1,2,3,4,5,6,7,8,0};

#     vector<vector<int>> solution = a_star(start_state, goal_state);

#     if (!solution.empty()) {
#         cout << "Steps to solve the puzzle:\n";
#         for (auto state : solution) print_state(state);
#     } else {
#         cout << "No solution found.\n";
#     }

#     return 0;
# }
