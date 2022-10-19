#!/usr/bin/env python
# coding: utf-8

# # Problem Statement - 2 ( Algorithms )
# Max Score: 50
# 
# ### Given a string str, your task is to write a program which takes a string str as its only input and returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.
# 
# ### Input Format:
# 
# ***The first and only line of input contains string str.***
# 
# ### Output Format:
# 
# ***The output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.***
# 
# #### Sample Input :
# 
# >abcdef
# 
# #### Sample Output :
# 
# >6
# 
# #### Explanation:
# 
# >For string 'abcdef' palindromic subsequence are : "a" ,"b", "c" ,"d","e","f"

# In[45]:
def countPsubs(i, j, s):
    if (i > j):
        #    Invalid substring.
        return 0
    if (i == j):
        return 1
    elif (s[i] == s[j]):
        return (1 + countPsubs(i + 1, j, s) + countPsubs(i, j - 1, s))
    else:
        return ((countPsubs(i + 1, j, s) + countPsubs(i, j - 1, s))- countPsubs(i + 1, j - 1, s))
def countPsubs1(s):
    return countPsubs(0, len(s) - 1, s)
countPsubs1("abcde")    
        
    
