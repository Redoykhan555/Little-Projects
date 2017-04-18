class DinnerDress:
    def __init__(self):
        self.shirt = 'white'
        self.pant = 'black'
        self.shoe = 'oxford'

class Uniform:
    def __init__(self):
        self.shirt = 'khaki'
        self.pant = 'khaki'
        self.shoe = 'oxford'

class Prayer:
    def __init__(self):
        self.shirt = 'white panjabi'
        self.pant = 'white payjama'
        self.shoe = 'sandal'

class Student:
    def __init__(self,dd,u,p):
        self.dinner = dd
        self.uni = u
        self.pr = p
        
import time
tt=time.clock()
dd,u,p = DinnerDress(),Uniform(),Prayer()
abc = []
for i in range(123456):
    temp = Student(dd,u,p)
    abc.append(temp)
print(time.clock()-tt)
