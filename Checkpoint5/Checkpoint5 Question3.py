class circle:
    def __init__(self,xycoord_center,r):
        self.xycoord_center=xycoord_center
        self.r=r
    def area(self):
        self.area=(self.r**2)*pi
        print(self.area)
    def perimeter(self):
        self.perimeter=self.r*2*pi
        print(self.perimeter)
    def isinside(self,point_coord):
        a=self.a=self.xycoord_center[0]
        b=self.b=self.xycoord_center[1]
        x=point_coord[0]
        y=point_coord[1]
        distance_center_point=((x-a)**2+(y-b)**2)**0.5
        if distance_center_point<self.r:
            print('the point with your coordinates is inside the circle')
        elif distance_center_point==self.r:
            print('the point with your coordinates is on the circumference of the circle')
        else:
            print('the point with your coordinates is outside of the circle')

circle=circle([4,0],2)
circle.isinside([5,7])
