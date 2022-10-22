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
def Pal_subs(i, j, s):
    if (i > j):
        return 0
    if (i == j):
        return 1
    elif (s[i] == s[j]):
        return (1 + Pal_subs(i + 1, j, s) + Pal_subs(i, j - 1, s))
    else:
        return ((Pal_subs(i + 1, j, s) + Pal_subs(i, j - 1, s))- Pal_subs(i + 1, j - 1, s))
def count_Pal_subs(s):
    return Pal_subs(0, len(s) - 1, s)
count_Pal_subs("abcde")    
        
    
