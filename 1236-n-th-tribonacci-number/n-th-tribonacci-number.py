class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[0,1,1]
        if n==0:
            return n
        elif n==1 or n==2:
            return 1
        else:
            for i in range(3,n+1):
                trib= arr[i-1]+ arr[i-2]+ arr[i-3]
                arr.append(trib)
        return arr[-1]
        