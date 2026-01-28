


def rectangle_overlap(l1,r1,l2,r2):
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False

    return True
    
print(rectangle_overlap((0,2),(1,1),(-2,0),(0,-3)))