#!/usr/bin/env python
# coding: utf-8

# In[3]:


(l,h)=map(int,input().split())
sum=0
for i in range(l,h+1):
    sum+=i
print(sum)


# In[5]:


n=int(input())
if n%400==0 or (n%4==0 and n%100!=0):
    print("leap")
else:
    print("non leap")


# In[15]:


n=int(input())
c=0
if n<2:
    c+=1
else:
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
            break
if c==1:
    print("not prime")
else:
    print("prime")


# In[20]:


n=int(input())
import math
c=0
if n<2:
    c+=1
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            c+=1
            break
if c==1:
    print("not prime")
else:
    print("prime")
        


# In[29]:


num=int(input())
flag = 0
if num<2:
  flag = 1
elif num == 2:
  flag = 0
else:
  for i in range(3,int(pow(num,0.5)+1),2):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")


# In[33]:


n=int(input())
def checkprime(n,iter=2):
    if n==iter:
        return True
    if n%iter==0:
        return False
    if n<2:
        return False
    return checkprime(n,iter+1)
if checkprime(n)==True:
    print("Prime")
else:
    print("Not Prime")
    
        
        


# In[34]:


(l,h)=map(int,input().split())
def primerange(l,h):
    prime=[]
    for i in range(l,h+1):
        c=0
        if i<2:
            continue
        elif i==2:
            prime.append(i)
            continue
        else:
            for j in range(2,i):
                if i%j==0:
                    c+=1
                    break
        if c==0:
            prime.append(i)
    return prime
print(primerange(l,h))
                
            
        


# In[3]:


(l,h)=map(int,input().split())
def prime_range(l,h):
    prime=[]
    for i in range(l,h+1):
        c=0
        iter=2
        if i<2:
            continue
        if i%2==0:
            #prime.append(i)
            continue
        #iter=2
        while iter<i//2+1:
                if i%iter==0:
                    c+=1
                    break
                iter+=1
        if c==0:
            prime.append(i)
    return prime
print(prime_range(l,h))
            


# In[ ]:





# In[16]:


n=int(input())
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)


# In[19]:


#print(str(n)[::-1])
n=int(input())
print(str(n)[::-1])


# In[30]:


number=int(input())
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
if sum==number:
  print("Armstrong")
else:
  print("Not Armstrong")


# In[2]:


l=int(input())
h=int(input())
for n in range(l,h+1):
    order=len(str(n))
    sum=0
    temp=n
    while temp>0:
        r=temp%10
        sum+=r**order
        temp//=10
    if n==sum:
        print(n)


# In[5]:


n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
    


# In[9]:


def facto(n):
    fact=1
    for i in range(n):
        return fact*fact(i-1)
print(facto(5))


# In[15]:


n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
def checkprime(n):
    c=0
    if n==0 or n==1:
        c+=1
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                c+=1
                break
    if c==1:
        return False
    else:
        return True
l1=[]
for i in l:
    if checkprime(i):
        l1.append(i)
print(*l1)    


# In[23]:


n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
sum=0
for i in range(len(l)):
    sum+=l[i]
if sum ==n:
    print("perfect")
else:
    print("not")


# In[32]:


from math import sqrt
def isperfect_square(n):
    if n>=0:
        sr=int(sqrt(n))
        return (sr*sr)==n
    return False
n=int(input())
if isperfect_square(n):
    print(True)
else:
    print(False)
if str(n**2).endswith(str(n)):
    print("Automorphic")
else:
    print("not")


# In[36]:


n=int(input())
n1=str(n)
n2=list(n1)
r=''
for i in range(len(n1)):
    if n2[i]=="0":
        n2[i]="1"
    r+=n2[i]
print(r)


# In[37]:


n=int(input())
n1=str(n)
r=n1.replace("0","1")
print(r)


# In[44]:


n=int(input())
l=[]
for i in range(2,n):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
            break
    if c==0:
        l.append(i)
for i in range(len(l)):
    for j in range(i):
        if l[i]+l[j]==n:
            print(l[j],l[i])


# In[46]:


def cnt_decoding_digits(dig,a):
    cnt=[0]*(a+1)
    cnt[0],cnt[1]=1,1
    for k in range(2,a+1):
        cnt[k]=0
        cnt[k]=cnt[k-1]
        if dig[k-2]=='1' or (dig[k-2]=='2' and dig[k-1]<'7'):
            cnt[k]+=cnt[k-2]
    return cnt[a]
dig=input()
print(cnt_decoding_digits(dig,len(dig)))


# In[50]:


def conv_to_words(num):
    l=len(num)
    if l==0:
        print("empty")
        return
    if l>4:
        print("more than 4 is not support")
        return
    single_dig=["zero","one","two","three","four","five", "six", "seven", "eight", "nine"]
    two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_power = ["hundred", "thousand"]
    print(num,":",end=" ")
    if l==1:
        print(single_dig[ord(num[0]-48)])
        return
    x=0
    while(x<len(num)):
        if l>=3:
            if ord(num[x]-48!=0):
                sum = (ord(num[x]) - 48 +ord(num[x+1]) - 48)
                print(two_digits[sum])
                return
 
            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return
 
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48])
        x += 1
 
 
# Driver Code
conv_to_words("1121")
                
        


# In[53]:


def isbalanced(s):
    c=0
    ans=False
    for i in s:
        if i==")":
            c+=1
        elif i=="(":
            c-=1
        if c<0:
            return ans
        if c==0:
            return not ans
    return ans
s=input()
print(isbalanced(s))


# In[54]:


n=int(input())
r=int(input())
l=list(map(int,input().split()))
class Solution:
    def rotate(self,l,r,n):
        a=l[r:n]
        b=l[0:r]
        c=a[:]
        for i in range(r):
            c.append(b[i])
        l[:]=c[:]
ob=Solution()
ob.rotate(l,r,n)
for i in l:
    print(i)

    
    


# In[58]:


n=int(input())
r=int(input())
l=list(map(int,input().split()))
def rotate(l,r,n):
    a=l[r:n]
    b=l[0:r]
    c=a[:]
    for i in range(r):
        c.append(b[i])
    l[:]=c[:]
    return l
print(rotate(l,r,n))


# In[61]:


def equilibrium(arr):
    leftsum=0
    rightsum=0
    n=len(arr)
    for i in range(n):
        leftsum=0
        rightsum=0
        for j in range(i):
            leftsum+=arr[j]
        for j in range(i+1,n):
            rightsum+=arr[j]
        if leftsum==rightsum:
            return i
    return -1
arr=list(map(int,input().split()))
print(equilibrium(arr))


# In[63]:


def equilibrium(arr):
    total_sum=sum(arr)
    leftsum=0
    for i,num in enumerate(arr):
        total_sum-=num
        if leftsum==total_sum:
            return i
        leftsum+=num
    return -1
arr=list(map(int,input().split()))
print(equilibrium(arr))


# In[67]:


def changearray(l):
    l1=l.copy()
    l1.sort()
    for i in range(len(l)):
        for j in range(len(l1)):
            if l[i]==l1[j]:
                l[i]=j+1
                break
    return l
l=list(map(int,input().split()))
print(changearray(l))


# In[77]:


l=list(map(int,input().split()))
l.sort()
print(l)
n=len(l)
mid=n//2
l1=[]
l2=[]
for i in range(0,mid):
    l1.insert(i,l[i])
for i in range(mid,n):
    l2.insert(i,l[i])
    l2.sort(reverse=True)


# In[80]:


def countdistinct(l,n):
    l.sort()
    i=0
    while i<n:
        count=1
        while i<n-1 and l[i]==l[i+1]:
            i+=1
            count+=1
        print("{0}:{1}".format(arr[i],count))
        i+=1
l=list(map(int,input().split()))
n=len(l)
print(countdistinct(l,n))


# In[82]:


def countfrequency(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        print(x," ",mp[x])
arr = [10, 30, 10, 20, 10, 20, 30, 10] 
n = len(arr) 
countfrequency(arr, n)


# In[86]:


from collections import Counter
l=list(map(int,input().split()))
res=[i for ic,c in Counter(l).most_common() for i in [ic]*c]
print(res)


# In[87]:


from collections import Counter
l=list(map(int,input().split()))
res=sorted(l,key=l.count,reverse=True)
print(res)


# In[89]:


def count(arr,n):
    mp=dict()
    count=0
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    print(len(mp))
arr=list(map(int,input().split()))
count(arr,n)


# In[90]:


def count(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        if mp[x]!=1:
            print(x)
arr=list(map(int,input().split()))
count(arr,n)


# In[91]:


l=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(l)):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("no of even number {}".format(len(e)))
print("no of odd numbers {}".format(len(o)))


# In[95]:


def sympairs(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
    for (y,x) in s:
        print((x,y))
pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
sympairs(pairs)


# In[98]:


def maxsum(arr):
    max=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>max:
            max=sum
    print(max)
arr=list(map(int,input().split()))
maxsum(arr)


# In[100]:


def maxSubarrayProduct(arr,n):
    max_ending_here=arr[0]
    min_ending_here=arr[0]
    max_so_far=arr[0]
    for i in range(n):
        temp=max({arr[i],arr[i]*max_ending_here,arr[i]*min_ending_here})
        min_ending_here=min({arr[i],arr[i]*max_ending_here,arr[i]*min_ending_here})
        max_ending_here=temp
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))


# In[102]:


def disjoint(l1,l2,m,n):
    l1.sort()
    l2.sort()
    i=0
    j=0
    while(i<m) and j<n:
        if l[i]<l2[j]:
            i+=1
        elif l2[j]<l1[i]:
            j+=1
        else:#l[i]==l2[j]
            return False
    return True
arr1 = [12, 34, 11, 9, 3]
arr2 = [7, 2, 1, 5]
m = len(arr1)
n = len(arr2)
 
print("Yes") if disjoint(arr1, arr2, m,n) else print("no")


# In[104]:


s=input()
s1="aeiouAIEOU"
if s in s1:
    print("vowel")
else:
    print("consonant")


# In[105]:


#ascii value
ord("a")


# In[107]:


#ascii to character
chr(100)


# In[108]:


s=input()
c=0
for i in s:
    c+=1
print(c)


# In[109]:


s=input()
s1=""
for i in s:
    if i.isupper():
        i=i.lower()
        s1+=i
    else:
        if i.islower():
            i=i.upper()
            s1+=i
print("{} changes to {}".format(s,s1))


# In[110]:


s=input()
print(s.swapcase())


# In[112]:


s=input()
s1="AEIOUaeiou"
c=0
for i in s:
    if i in s1:
        c+=1
print(c)


# In[113]:


s=input()
s1="AEIOUaeiou"
s2=""
for i in s:
    if i not in s1:
        s2+=i
print(s2)
        


# In[115]:


s=input()
s1=s[::-1]
if s==s1:
    print("palindrome")
else:
    print("not")


# In[116]:


s=input()
s1="abcdefghijklmnopqrstuvwxyz"
s2=""
for i in s:
    if i in s1:
        s2+=i
print(s2)


# In[117]:


s=input()
print(s.replace(" ",""))


# In[118]:


s=input()
s1="()"
s2=""
for i in s:
    if i not in s1:
        s2+=i
print(s2)


# In[120]:


s=input()
s1=int(s)
print(eval(s1))


# In[124]:


s=input()
s1="123456789"
s2=[]
for i in s:
    if i in s1:
        s2.append(i)
print(s2)
sum=0
for i in s2:
    sum+=int(i)
print(sum)


# In[127]:


string=input()
string=string[0:1].upper()+string[1:len(string)-1]+string[len(string)-1:len(string)].upper()
print(string)


# In[129]:


s=input()
for i in s:
    freq=s.count(i)
    print(str(i)+":"+str(freq),end=" ")


# In[130]:


s=input()
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


# In[133]:


s=input()
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
        if c>1:
            break
    if c==1:
        print(i,end="")
       


# In[136]:


s=input()
s1=input()
if sorted(s)==sorted(s1):
    print("anagram")
else:
    print("not")


# In[139]:


from collections import Counter
def check(s1,s2):
    print(Counter(s1))
    print(Counter(s2))
    if Counter(s1)==Counter(s2):
        print("anagram")
    else:
        print("not")
s=input()
s1=input()
check(s,s1)


# In[140]:


s=input()
s1=input("enter which has to be replaced")
s2=input("enter with replace substring")
s=s.replace(s1,s2)
print(s)


# In[142]:


s=input()
s1=input("enter which has to be replaced")
for i in s:
    if i in s1:
        print(s.index(i))


# In[144]:





# In[145]:


ans=[]
def permute(a,l,r):
    if l==r:
        ans.append("".join(a))
    else:
        for i in range(l,r):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]
string="ABC"
n=len(string)
a=list(string)
permute(a,0,n)
for i in sorted(ans):
    print(i)


# In[147]:


l=list(map(int,input().split()))
def count(l):
    count_0=l.count(0)
    count_1=l.count(1)
    count_2=l.count(2)
    l1=[]
    for i in range(count_0):
        l1.append(0)
    for i in range(count_1):
        l1.append(1)
    for i in range(count_2):
        l1.append(2)
    return l1
count(l)


# In[150]:


l=list(map(int,input().split()))
l.sort()
print(l)


# In[152]:


l=list(map(int,input().split()))
k=int(input())
n=len(l)
l.sort()
print(l[k])


# In[153]:


l=list(map(int,input().split()))
l1=list(map(int,input().split()))
def union(l1,l2):
    l1=set(l1)
    l2=set(l2)
    print(l1 | l2)
def intersection(l1,l2):
    l1=set(l1)
    l2=set(l2)
    print(l1&l2)
union(l1,l2)
intersection(l1,l2)


# In[154]:


def find(arr,l):
    max=0
    sum=0
    for i in range(l):
        sum+=arr[i]
        if sum>max:
            max=sum
    print(max)
arr=list(map(int,input().split()))
l=len(arr)
find(arr,l)


# In[157]:


def findsubarraymax(arr,l):
    max_sum=-1
    ans=[]
    for i in range(l):
        for j in range(i,l):
            a=sum(array[i:j+1])
            if a>max_sum:
                max_sum=a
                ans=array[i:j+1]
    print(ans)
    print(max_sum)
array=list(map(int,input().split()))
l=len(array)
findsubarraymax(array,l)


# In[160]:


def find(arr, l):
    max_sum = -1
    ans = []
    for i in range(l):
        for j in range(i, l):
            a = sum(arr[i:j + 1])
            if a > max_sum:
                max_sum = a
                ans = arr[i:j + 1]

    print("Sub array which will give maximum sum", ans)
    print("Maximum sum = ", max_sum)


array = [-1, 8, 1, -7, -1, 5, 1, -3]
print("Array =", array)
find(array, len(array))


# In[159]:


def profit(arr,k):
    n=(min(arr)+max(arr))//2
    new=[]
    for i in arr:
        if max(arr)-min(arr)<k:
            return max(arr)-min(arr)
        elif i>=n:
            new.append(i-k)
        else:
            new.append(i+k)
    return max(new)-min(new)
array=[2,9,16]
k=6
profit(arr,k)
    


# In[164]:


def jump(arr):
    n=len(arr)
    i=0
    c=0
    while i<len(arr)-1:
        if i+arr[i]<n:
            c+=1
            if arr[i]==1:
                i+=arr[i]
            else:
                i+=arr.index(max(arr[i+1:arr[i]+i+1]))-i
        else:
            c+=1
            i+=arr[i]
    return c
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Minimum no of jumps required to reach end of the array : ", jump(arr))


# In[ ]:




