# Private Attribute and Method -> it meant to only within the class and are not accessible from outside the class
# __name = "Aman"-> private data 
# def __hello() :
#     print("Hello") -> private method



class Account :
    def __init__(self,acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # -> Private "__" class define way

    def reset_pass(self):
        print(self.__acc_pass) #-> we can acess 



acc1 = Account("12345","abcd")   
print(acc1.acc_no)     
print(acc1.__acc_pass)    # -> we can't access pass
