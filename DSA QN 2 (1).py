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

# In[3]:


"""
    Time Complexity: O(2^N)
    Space Complexity: O(N)

    where 'N' is the length of the string.
"""


#    Returns the number of palindromic subsequences in the substring [i: j] of string ‘s’.
def countPsubs(i, j, s):

    if (i > j):
        #    Invalid substring.
        return 0

    if (i == j):
        #    Every single character in the string is a palindrome itself.
        return 1

    elif (s[i] == s[j]):
        return (1 + countPsubs(i + 1, j, s) + countPsubs(i, j - 1, s))
    else:
        return ((countPsubs(i + 1, j, s) + countPsubs(i, j - 1, s))- countPsubs(i + 1, j - 1, s))
def countPsubs1(s):

    return countPsubs(0, len(s) - 1, s)

countPsubs1("abcde")    
        
    


# In[11]:


def countPS(str):
 
    N = len(str)
 
    # Create a 2D array to store the count
    # of palindromic subsequence
    cps = [[0 for i in range(N + 2)]for j in range(N + 2)]
 
    # palindromic subsequence of length 1
    for i in range(N):
        cps[i][i] = 1
 
    # check subsequence of length L
    # is palindrome or not
    for L in range(2, N + 1):
 
        for i in range(N):
            k = L + i - 1
            if (k < N):
                if (str[i] == str[k]):
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] + 1)
                else:
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] -
                                 cps[i + 1][k - 1])
 
    # return total palindromic subsequence
    return cps[0][N - 1]


# Driver program
str = "aaa"
print(countPS(str))


# In[ ]:


"""
    Time Complexity: O(2^N)
    Space Complexity: O(N)

    where 'N' is the length of the string.
"""

# mod = (10 ** 9) + 7

#    Returns the number of palindromic subsequences in the substring [i: j] of string ‘s’.
def countPS(i, j, s):

    if (i > j):

        #    Invalid substring.
        return 0

    if (i == j):

        #    Every single character in the string is a palindrome itself.
        return 1

    elif (s[i] == s[j]):
        return (1 + countPS(i + 1, j, s) + countPS(i, j - 1, s))
#         return (1 + countPS(i + 1, j, s) + countPS(i, j - 1, s)) % mod
    else:
        return ((countPS(i + 1, j, s) + countPS(i, j - 1, s))- countPS(i + 1, j - 1, s) )
#         return ((countPS(i + 1, j, s) + countPS(i, j - 1, s)) % mod - countPS(i + 1, j - 1, s) + mod) % mod

def countPalindromicSubseq(s):

    return countPS(0, len(s) - 1, s)

countPalindromicSubseq("aaa")    
        

