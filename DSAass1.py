#!/usr/bin/env python
# coding: utf-8
'''Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

Q3. Write a program to check if two strings are a rotation of each other?

Q4. Write a program to print the first non-repeated character from a string?

Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

Q7. Write a program to convert prefix expression to infix expression.

Q8. Write a program to check if all the brackets are closed in a given code snippet.

Q9. Write a program to reverse a stack.

Q10. Write a program to find the smallest number using a stack.'''

# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
# 

# In[16]:


def twosum(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+array[j]==10:
                print((arr[i],arr[j]))              
            else:
                continue
    return

twosum([1,2,3,4,5,6,7,8,9,0],10)


# In[43]:


def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<right):
        if(arr[left]+arr[right]>sum):
            right=right-1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        elif(arr[left]+arr[right]==sum):
            print((arr[left],arr[right]))
            left=left+1
            right=right-1
twosum([1,2,3,4,5,6,7,8,9,0],10)          
        


# # Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[18]:


def reversearr(arr):
    arr.reverse()
    return arr
arr=list(map(int,input().split()))
reversearr(arr)
            
        


# In[1]:





# # Q3. Write a program to check if two strings are a rotation of each other?

# In[5]:


s1="helloworld"
s2="worldhello"
class Rotate:
    def rotation(s1,s2):
        if len(s1)==len(s2):
            s3=s1+s1
            
            if s2 in s3:
                print('passed')
                return True
            else:
                return False
        else:
            return False
x=Rotate
x.rotation(s1,s2)



# # Q4. Write a program to print the first non-repeated character from a string?
# 

# In[6]:


def nonrepeatedchar(st):
    d={}
    for i in st:
        if d.get(i):
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
            return i
st="abhinav"
nonrepeatedchar(st)        
    
            
        
        


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# 

# In[41]:


def TOH(num,start,end,aux):
    if num==1:
        print("moved disk 1 from pole {} to pole {}".format(start,end))
        return
    TOH(num-1,start,aux,end)
    print("moved disk {} from pole {} to pole {}".format(num,start,end))
    TOH(num-1,aux,end,start)
    
disk=3
TOH(disk,"A","B","C")


# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# 

# In[34]:


class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        return self.arr.pop()
def post_to_pre(postfixEx):
    stack = Stack()
    l = postfixEx
    for i in l:
        if i.isalnum():
            stack.push(i)
             
        else:
            o2 = stack.pop()
            o1 = stack.pop()
            result = calculation(i,o1,o2)
            stack.push(result) 
            
    return stack.pop()
def calculation(i,j,k):
    return i+j+k
print(postfixEval('AB+CD-*'))

# *+AB-CD


# # Q7. Write a program to convert prefix expression to infix expression.
# 

# In[49]:


class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        return self.arr.pop()
def pre_to_inf(prefixEx):
    stack=Stack()
    l=prefixEx
    for i in range(-1,-len(l)-1,-1):
        if l[i] not in "+-/*^()":
            stack.push(l[i])
        else:
            x="("+ stack.pop() + l[i] + stack.pop() +")"
            stack.push(x)
    return stack.pop()
pre_to_inf("*-A/BC-/AKL")          
    
    


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.
# 

# In[53]:


def Balanced(s):
    stack=[]
    
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            stack.append(s[i])
        elif len(stack)!=0 and ((stack[-1]=='(' and s[i]==')') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='{' and s[i]=='}')):
            stack.pop()
        else:
            return "NO"
    if  len(stack)==0:
        return "Balanced"
    else:
        return "Not Balanced"
Balanced("{()[({})]}")


# # Q9. Write a program to reverse a stack.
# 

# In[ ]:


class Stack :
    def __init__(self):
        self.arr = []
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        if len(self.arr)==0:
            print("stack is empty")
            return
        return self.arr.pop()
    
            
s=Stack()
def reverse(s):
        for i in range(len(s.arr)):
            print(s.pop())
        return 
s.push(10)
s.push(20)
s.push(30)
s.push(40)
reverse(s)


# # Q10. Write a program to find the smallest number using a stack.

# In[2]:


class Stack :
    def __init__(self):
        self.arr = []
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        return self.arr.pop()
        
    def smallest(self):
        self.arr.sort()
        return self.arr[0]
        
            
s=Stack()
s.push(30)
s.push(10)
s.push(20)
s.push(40)
s.smallest()


# In[ ]:




