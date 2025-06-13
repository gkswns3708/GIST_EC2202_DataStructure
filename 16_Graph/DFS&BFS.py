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


# --- 사용 예시 ---
if __name__ == "__main__":
    # 예시 1: 연결 그래프
    edges1 = [
        (0, 1), (0, 2), (1, 2), (2, 3)
    ]
    g1 = build_graph(edges1)
    print("DFS Recursive from 0:", dfs_recursive(g1, 0))
    print("DFS Iterative from 0:", dfs_iterative(g1, 0))
    print("BFS from 0:", bfs(g1, 0))

    # 예시 2: 단절된 그래프
    edges2 = [
        (1, 2), (2, 0), (0, 3),    # 컴포넌트 A
        (4, 5)                     # 컴포넌트 B
    ]
    g2 = build_graph(edges2)
    print(g2,"- g2")
    print("Full DFS:", dfs_full(g2))
    print("Full BFS:", bfs_full(g2))