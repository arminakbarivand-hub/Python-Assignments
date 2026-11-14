a = int(input())
b = int(input())
c = int(input())
if 1 <= a <= 150 and 1<= b <= 150 and 1<= c <= 150 :
    if b*b == (c*c) + (a*a) : 
        print ("YES")
    elif c*c == (a*a) + (b*b) :
        print ("YES")
    elif a*a == (b*b) + (c*c) :
        print("YES")
    else : print ("NO")
else : print(" invalid input")