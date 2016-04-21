'''
Created on 20 avr. 2016

@author: tarek
'''

class Point:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def moyenne(self,p1,p2):
        
        self.x = (p1.x+p2.x)/2
        self.y = (p1.y+p2.y)/2
        
        
if __name__ == '__main__':
    print("Hello main method")
        
    p1 = Point(1.0,1.0)
    p2 = Point(4.0,4.0)
    
    p3 = Point(0.0,0.0)
    p3.moyenne(p1, p2)
    print(p3.x)
    print(p3.y)