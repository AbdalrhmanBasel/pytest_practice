# Python program to find the area of a triangle
def area_of_triangle(s1, s2, s3):
    area = s1 + s2 + s3 / 2
    return area


s1 = int(input("Side #1: "))
s2 = int(input("Side #2: "))
s3 = int(input("Side #3: "))

print(area_of_triangle(s1, s2, s3))
