"""
Refer codingbat.com/prob/p118406

Sample:
make_bricks(3,1,8)  = True
make_bricks(3,1,9)  =False
make_bricks(3,2,10) = True

small brick of length 1. Big of 5. Aim is to create brick of goal lenght using small and big bricks

"""
def make_bricks(small, big, goal):
     if (goal//5 <=big) and goal-5*(goal//5)<=small: return True
     elif (goal//5 >= big) and goal-5*big<=small: return True
     return False

s=make_bricks(3, 4, 56)
print s

