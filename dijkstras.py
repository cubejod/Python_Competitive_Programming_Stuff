'''
dijkstras using priority queue
many many modifications can be done depending on the problem
n= number of points
r= edges
s= start
d= end
'''

import heapq
cases = int(input())
for i in range(cases):
    shortest={}
    n,r,s,d=map(int,input().split())
    adj={}
    visited={}
    pq=[]
    for j in range(r):
        u,v,t=map(int,input().split())
        if u in adj:
            adj[u].append([v,t])
        else:
            adj[u]=[[v,t]]
        if v in adj:
            adj[v].append([u,t])
        else:
            adj[v]=[[u,t]]
    heapq.heappush(pq,[0,s])
    while pq:
        d1,n1=heapq.heappop(pq)
        if n1 in shortest:
            continue
        shortest[n1]=d1
        for n2, d2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(pq,[d1+d2+12,n2])
    print(shortest[d])