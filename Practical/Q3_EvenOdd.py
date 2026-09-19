class Solution : 
    def __init__(self,n) :
        self.n = n

    def check_num(self) :
        if(self.n%2==0) :
            return True

        else :
            return False



if __name__ == "__main__" :
    n = int(input("Enter a value : "))

    obj = Solution(n)
    print(obj.check_num())
