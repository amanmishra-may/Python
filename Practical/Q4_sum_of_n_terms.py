class Solution :
    def __init__(self,num,sum) :
        self.num = num 
        self.sum = sum
        
    def Sum_nterm(self) :
        for i in range (1,self.num+1):
            self.sum = self.sum+ i

        return self.sum



if __name__ == "__main__" :
    sum = 0
    num = int(input("Enter a number : "))
    obj = Solution(num,sum)
    print(obj.Sum_nterm())
    


