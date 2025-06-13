import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def add_edge(adj, u, v):
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

def build_graph(edges):
    adj = {}
    for u, v in edges:
        add_edge(adj, u, v)
    return adj

# 전역 변수 (초기화는 __main__ 블록에서 수행)
adj = {}
visited = []
order = []
cnt = 0

if __name__ == "__main__":
    def dfs_recursive(node):
        global cnt
        visited[node] = True
        cnt += 1
        order[node] = cnt
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs_recursive(neighbor)

    # 입력 처리
    N, M, R = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # 그래프 구축 및 정렬
    adj = build_graph(edges)
    for i in range(1, N+1):
        adj.setdefault(i, [])
    for node in adj:
        adj[node].sort()

    visited = [False] * (N + 1)
    order   = [0]     * (N + 1)
    cnt = 0

    dfs_recursive(R)
    print('\n'.join(str(order[i]) for i in range(1, N+1)))
