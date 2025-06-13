import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 좌표 → node id 변환
def nid(x, y, M):
    return y * M + x

# BFS로 하나의 연결 요소를 순회하며 방문 처리
def bfs_component(graph, start, visited):
    q = deque([start])
    visited.add(start)

    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)

# 테스트케이스 처리
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for _ in range(K)]
    
    # 배추 위치 집합
    pos_set = set(cabbages)
    
    # 상하좌우 인접한 배추들 사이에 간선 추가
    edges = []
    for x, y in cabbages:
        u = nid(x, y, M)
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in pos_set:
                v = nid(nx, ny, M)
                edges.append((u, v))
    
    # 인접 리스트 그래프 생성
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    # (옵션) 이웃 순회할 때 항상 작은 번호부터 방문하게 정렬
    for nbrs in graph.values():
        nbrs.sort()
    
    # BFS로 연결 요소 개수 세기
    visited = set()
    worms_needed = 0
    for x, y in cabbages:
        u = nid(x, y, M)
        if u not in visited:
            worms_needed += 1
            bfs_component(graph, u, visited)
    
    print(worms_needed)
