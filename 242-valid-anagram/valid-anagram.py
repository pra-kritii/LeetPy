class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # list1=list(s)
        # list2=list(t)

        # list1.sort()
        # list2.sort()

        # if list1==list2:
        #     return True
        # return False

        if len(s) != len(t):
            return False

        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for i in t:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]-=1

        for i in freq.values():
            if i!=0:
                return False
        return True