import sys
from collections import deque
input = sys.stdin.readline

def add_edge(adj, u, v):
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

def build_graph(edges):
    adj = {}
    for u, v in edges:
        add_edge(adj, u, v)
    return adj

adj = {}
visited = []
order = []
cnt = 0

if __name__ == "__main__":
    # — 알고리즘: 너비 우선 탐색 (여기에 몰아넣음)
    def bfs(start):
        global cnt
        visited[start] = True
        cnt += 1
        order[start] = cnt
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    cnt += 1
                    order[v] = cnt
                    q.append(v)

    N, M, R = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    adj = build_graph(edges)
    for i in range(1, N + 1):
        adj.setdefault(i, [])
    for node in adj:
        adj[node].sort()

    visited = [False] * (N + 1)
    order   = [0]     * (N + 1)
    cnt = 0

    bfs(R)
    print('\n'.join(str(order[i]) for i in range(1, N + 1)))
