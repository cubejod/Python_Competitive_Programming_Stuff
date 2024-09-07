'''
solves leetcode 547 https://leetcode.com/problems/number-of-provinces/description/?envType=problem-list-v2&envId=union-find
prints # of connected 
'''



class Solution:
    def findCircleNum(self, isConnected):
        parent=[i for i in range(0,len(isConnected))]
        rank=[1]*len(isConnected)
        def find(n1):
            while parent[n1]!=n1:
                n1=parent[n1]
                parent[n1]=parent[parent[n1]]
            return n1
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                #merge p2 into p1
                parent[p2]=p1
                rank[p1]+=rank[p2]
                return 1
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
                return 1
        #below lines are NOT used in the algorithm, only for the leetcode problem
        output=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    output-=union(i,j)
        return output
    

asdf=Solution()
print(asdf.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))