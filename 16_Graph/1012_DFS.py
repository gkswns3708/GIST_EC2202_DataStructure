import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

# --- 주어진 그래프 유틸 코드 ---
def add_edge(adj, u, v):
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

def build_graph(edges):
    adj = {}
    for u, v in edges:
        add_edge(adj, u, v)
    return adj

def dfs_recursive(graph, node, visited):
    visited.add(node)
    for nei in graph.get(node, []):
        if nei not in visited:
            dfs_recursive(graph, nei, visited)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for _ in range(K)]
    # 1) 좌표 → node id 변환 함수
    def nid(x, y): return y * M + x
    
    # 2) 배추 위치 집합과 간선 리스트 구축
    pos_set = set(cabbages)
    edges = []
    for x, y in cabbages:
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in pos_set:
                edges.append((nid(x,y), nid(nx,ny)))
    
    # 3) 그래프 생성
    graph = build_graph(edges)
    
    # 4) 연결 요소 개수 세기
    visited = set()
    count = 0
    # 모든 node id 순회 (isolated도 있기에 pos_set 기준)
    for x, y in cabbages:
        u = nid(x, y)
        if u not in visited:
            count += 1
            dfs_recursive(graph, u, visited)
    print(count)
