class Solution:  
    def addDigits(self, num: int) -> int:
        if(num==0):
            return 0 
          
        def fun(num):
            r=0           
            for i in range(0,len(str(num))):
                r+=int(str(num)[i])
            if(r>0 and r<=9):
                return r
            else:
                num=r
                return fun(num)
        return fun(num) 
