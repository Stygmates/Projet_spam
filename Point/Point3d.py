'''
Created on 20 avr. 2016

@author: tarek
'''

class Point3d:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self,x,y,z,spam):
        self.x = x
        self.y = y
        self.z = z
        self.spam = spam
        
    def moyenne(self,p1,p2):
        
        self.x = (p1.x+p2.x)/2
        self.y = (p1.y+p2.y)/2
        self.z = (p1.z+p2.z)/2        
        
if __name__ == '__main__':
    print("Hello main method")
        
    p1 = Point3d(1.0,1.0,5.0,0)
    p2 = Point3d(4.0,4.0,4.0,0)
    
    p3 = Point3d(0.0,0.0,3.0,0)
    p3.moyenne(p1, p2)
    print(p3.x)
    print(p3.y)