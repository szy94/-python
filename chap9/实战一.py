class Circle(object):
    def __init__(self,r):
        self.r=r
    #计算面积的方法
    def get_area(self):
        # return 3.14*self.r*self.r
        return 3.14*pow(self.r,2)
    #计算圆的周长
    def get_perimeter(self):
        return 2*3.14*self.r
r=eval(input(' 请输入圆的半径：'))
c=Circle(r)
area=c.get_area()
perimeter=c.get_perimeter()
print(area)
print(perimeter)
