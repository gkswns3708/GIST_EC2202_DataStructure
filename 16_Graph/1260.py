import sys
from collections import defaultdict
# 그래프 표현: 인접 리스트 (Undirected Unweighted Graph)
def add_edge(adj, u, v):
    """u와 v 사이에 간선을 추가 (무향)"""
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

def build_graph(edges):
    """간선 리스트로부터 그래프(인접 리스트) 생성"""
    adj = {}
    for u, v in edges:
        add_edge(adj, u, v)
    return adj


# DFS (재귀)
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


# DFS (반복, 스택 이용)
def dfs_iterative(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # insertion 순서 대로 방문하려면 역순으로 쌓기
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


# BFS (큐 이용)
from collections import deque

def bfs(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


# 전체 노드를 모두 방문하는 DFS/BFS (그래프가 단절된 경우)
def dfs_full(graph):
    visited = []
    for node in graph:
        print(node, "- node")
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def bfs_full(graph):
    visited = []
    for node in graph:
        if node not in visited:
            visited.extend(bfs(graph, node))
    return visited

if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().rstrip().split())
    edges = []
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        edges.append((u, v))
    graph = build_graph(edges)
    # 각 노드의 인접 리스트를 오름차순 정렬
    for k in graph:
        graph[k].sort()
    dfs_result = dfs_recursive(graph, V)
    # dfs_result = dfs_iterative(graph, V)
    bfs_result = bfs(graph, V)
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))
    