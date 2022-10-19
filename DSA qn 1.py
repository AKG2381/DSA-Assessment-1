#!/usr/bin/env python
# coding: utf-8

# # Problem Statement - 1 (Data Structure)
# Max Score: 50
# 
# ### You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the input graph starting from node x. Complete the following function in order to give the required output.
# 
# ### Input Format:
# 
# ***The first line of input contains a list containing sets representing a graph. The second line of input contains the number x.*** 
# 
# ### Output Format:
# 
# ***Complete the function in order to return the required output.***
# 
# #### Sample Input 0:
# 
# >[[1,0],[2,0],[3,0],[3,2]]
# 
# >3
# 
# #### Sample Output 0:
# 
# >3 0 2 

# In[44]:

# creating a graph
n=int(input("Enter the number of elemnts:: "))
graph=[]
for i in range(n):
    graph.append(list(map(int,input("enter two elements as space seperated ").split())))
x=[]                                        # getting list of all vertex
for i in graph:
    x.extend(i)
vertex=list(set(x))
# print(vertex)

d = {}                                       # creating the graph as a dictionary from the user inout nested list
for a, b in graph:
    d.setdefault(a, []).append(b)
# print(d)
for v in vertex:
        if v not in d:
#             print(v)
            d[v] = []
# print(d)
visited=set()
root=int(input("enter the root node"))        # starting node for trversing
def DFS(visited,graph,root):                  # implementing depth-first-search (DFS)
    
    if root not in visited:
        print(root,end=' ')
        visited.add(root)
#         print(visited)
        for i in set(d[root])-visited:
            DFS(visited,graph,i) 
DFS(visited,graph,root)




