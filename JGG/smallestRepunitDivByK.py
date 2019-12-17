class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        k = K
        if k%2==0 or k%5 ==0:
            return -1
        else:
            x = 1
            res = 1
            while(x%k !=0):
                x = x%k * 10 + 1
                res+=1
        return res
