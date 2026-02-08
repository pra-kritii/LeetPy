class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # for i in range(0,31):
        #     ans = pow(2,i)
        #     if ans==n:
        #         return True
        # return False


        if n<=0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        return self.isPowerOfTwo(n//2)
