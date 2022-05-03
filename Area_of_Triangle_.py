a,b,c=map(int,input().split())
# calculate the semi-perimeter
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('%0.2f' %area)