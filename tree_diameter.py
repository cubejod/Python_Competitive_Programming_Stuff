'''
this one is cool
it does a BFS on an arbitrary node and then does a BFS on the farthest node found by the first BFS
somehow the two nodes found are on the diameter

input:
 line 1 = number of nodes
 next n-1 lines = a,b (there is edge from a to b)
'''
from collections import deque

edges = int(input())
adj = {}
for i in range(edges - 1):
    edge = list(map(int, input().split()))
    if edge[0] in adj:
        adj[edge[0]].append(edge[1])
    else:
        adj[edge[0]] = [edge[1]]
    if edge[1] in adj:
        adj[edge[1]].append(edge[0])
    else:
        adj[edge[1]] = [edge[0]]
gHeight = 0
ghn = 0


def bfs(queue):
    global gHeight
    global ghn
    seen = {}
    while len(queue) > 0:
        node = queue.popleft()
        if node[0] not in seen:
            seen[node[0]] = 1
        else:
            continue
        if node[1] > gHeight:
            gHeight = node[1]
            ghn = node[0]
        if node[0] in adj:
            for i in range(len(adj[node[0]])):
                if adj[node[0]][i] not in seen:
                    queue.append([adj[node[0]][i], node[1] + 1])


bfs(deque([[1, 0]]))
bfs(deque([[ghn, 0]]))
print(gHeight)