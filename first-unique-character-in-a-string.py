class Solution:
    def firstUniqChar(self, s):
        ht={}
        for i in s:
            if i in ht:
                ht[i]+=1
            else:
                ht[i]=1
        for i in range (len(s)):
            if ht[s[i]]==1:
                return i
        return -1
        
