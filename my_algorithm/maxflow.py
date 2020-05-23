
#https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

import sys
import collections

class MaxFlow():
    def __init__(self, node, source, destination, edge_pairs = None, edge_marix = None):
        self.node = node
        self.edge_pairs = edge_pairs
        self.edge_marix = edge_marix
        self.s = source
        self.t = destination
        self.rflow = None
    
    def find_path(self):
        
        parent = [0] * self.node
        visit = [False] * self.node
        for i in range(self.node):
            parent[i] = i

        q = collections.deque()
        q.append(self.s)
        visit[self.s] = True

        while(len(q) > 0):
            cur = q.popleft()
            if cur == self.t:
                return parent
        
            for j in range(self.node):
                if self.rflow[cur][j] > 0 and visit[j] == False:
                    q.append(j)
                    parent[j] = cur
                    visit[j] = True
        
        return None

    
    def init_resudue_flow_matrix(self):
        self.rflow = [ [0] * (len(self.edge_marix[0]) + 1) for i in range(len(self.edge_marix) + 1)  ]
        for i in range(len(self.edge_marix)):
            for j in range(len(self.edge_marix[0])):
                self.rflow[i][j] = self.edge_marix[i][j]
    
    def update_resedue_flow(self, parent):
        node = self.t
        min_flow =  2**30
        while(parent[node] != node):
            parent_node = parent[node]
            min_flow = min(min_flow, self.rflow[parent_node][node])
            node = parent_node
        
        node = self.t
        while(parent[node] != node):
            parent_node = parent[node]
            self.rflow[parent_node][node] = self.rflow[parent_node][node] - min_flow
            self.rflow[node][parent_node] = self.rflow[node][parent_node] + min_flow
            node = parent_node

        return min_flow

            
    def find_maxflow_adj_mat(self):
        self.init_resudue_flow_matrix()
        max_flow = 0
        while (True):
            path = self.find_path()
            if (path == None):
                break
            
            cur_flow = self.update_resedue_flow(path)
            max_flow = max_flow + cur_flow
        
        return max_flow

    def find_maxflow_adj_list(self):
        pass

    def get_maxflow(self):
        if (self.edge_marix != None):
            return self.find_maxflow_adj_mat()
        
        return self.find_maxflow_adj_list()
    


def Test():
    edge_mat = [ [0, 16, 13, 0, 0, 0], 
                        [0, 0, 10, 12, 0, 0], 
                        [0, 4, 0, 0, 14, 0], 
                        [0, 0, 9, 0, 0, 20], 
                        [0, 0, 0, 7, 0, 4], 
                        [0, 0, 0, 0, 0, 0] 
            ]
  
    flow = MaxFlow(6, 0, 5, edge_marix=edge_mat)
    f = flow.get_maxflow()
    print(f)

Test()
